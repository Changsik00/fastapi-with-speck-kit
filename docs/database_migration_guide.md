# Alembic 마이그레이션 가이드 및 안전 수칙

이 문서는 데이터베이스 스키마 변경을 안전하게 관리하기 위한 **운영 매뉴얼**입니다.
Alembic은 강력하지만, 잘못 사용하면 **데이터 손실**이나 **서비스 장애(Table Lock)**를 유발할 수 있습니다.

---

## 1. 기본 명령어 (Basic Commands)

가장 자주 사용하는 명령어들입니다.

| 명령어 | 설명 | 비고 |
|---|---|---|
| `uv run alembic current` | **현재 상태 확인**. DB가 어떤 리비전까지 적용되어 있는지 보여줍니다. | 작업 전 필수 확인 |
| `uv run alembic history` | 전체 마이그레이션 히스토리(순서)를 보여줍니다. | |
| `uv run alembic upgrade head` | DB를 최신 버전(`head`)으로 동기화합니다. | **주의**: 운영 환경 배포 시 자동 실행 여부 신중 결정 |
| `uv run alembic downgrade -1` | 바로 이전 버전으로 롤백합니다. | 비상 시 사용 |

---

## 2. 작업 워크플로우 (Workflow)

1.  **모델 수정**: `models.py`에서 SQLModel 클래스를 수정합니다.
2.  **리비전 생성**: `uv run alembic revision --autogenerate -m "메시지"`
3.  **스크립트 검토 (중요!)**: 생성된 `versions/xxxx_my_change.py` 파일을 열어서 확인합니다.
    *   Alembic이 의도치 않은 `drop_table`이나 `drop_column`을 만들지 않았는지 확인하세요.
4.  **적용 및 테스트**: 로컬에서 `upgrade head`를 실행하고 테스트합니다.

---

## 3. ⚠️ 위험 관리 및 주의사항 (Critical Risks)

**"같은 테이블에서 스키마를 수정하는 것은 매우 리스키한 일입니다."**

### 3.1. `alter_column`의 위험성
`alembic`이 생성해주는 `op.alter_column` 명령어는 다음과 같은 위험이 있습니다:
1.  **Table Lock**: 컬럼 타입을 변경하거나 제약조건을 걸 때, 테이블 전체가 잠길(Lock) 수 있습니다. 데이터가 많은 운영 DB에서는 서비스가 멈출 수 있습니다.
2.  **데이터 손실/형변환 실패**: `VARCHAR`를 `INTEGER`로 바꾸는 등 형변환이 불가능한 데이터가 있으면 마이그레이션이 실패하거나 데이터가 엉망이 될 수 있습니다.

### 3.2. 운영 DB 배포 전 체크리스트
- [ ] 마이그레이션 스크립트에 `DROP COLUMN`, `DROP TABLE`이 포함되어 있지 않은가?
- [ ] 데이터가 있는 상태에서 `NOT NULL` 제약조건을 추가하는가? (기존 데이터는 NULL인데 NOT NULL을 걸면 실패함)
- [ ] 테이블 사이즈가 큰가? (크다면 점검 필요)

---

## 4. 안전한 마이그레이션 패턴 (Expand and Contract)

운영 중인 대규모 DB에서 컬럼을 안전하게 변경하려면 **"Expand and Contract(확장 후 축소)"** 패턴을 사용해야 합니다.

### 예시: `address` 컬럼의 이름을 `full_address`로 바꾸고 싶을 때

❌ **나쁜 방법 (한 방에 수정)**:
```python
op.alter_column('users', 'address', new_column_name='full_address')
# DB Lock 발생, 배포 전까지 구버전 코드는 에러 발생
```

✅ **좋은 방법 (Expand and Contract)**:

1.  **Expand (확장)**:
    - 새로운 컬럼 `full_address`를 `Nullable`로 추가합니다. (`add_column`)
    - 기존 `address`는 그대로 둡니다.
    - 배포합니다. (서비스 영향 없음)

2.  **Migrate Data (데이터 이동)**:
    - 백그라운드 스크립트나 코드 레벨에서 `address`의 값을 `full_address`로 복사합니다.
    - 새로 들어오는 데이터는 `address`와 `full_address` 양쪽에 쓰도록 코드를 수정합니다(Dual Write).

3.  **Execute (전환)**:
    - 코드가 `full_address`만 읽도록 수정하여 배포합니다.

4.  **Contract (축소)**:
    - 더 이상 쓰이지 않는 `address` 컬럼을 삭제(`drop_column`)합니다.

이 방식은 시간은 걸리지만 **무중단**으로, **데이터 손실 위험 없이** 스키마를 변경하는 가장 안전한 방법입니다.

---

## 5. 🛑 데이터 손실 방지 정책 (Anti-Drop Policy)

**"우리는 어떤 경우에도 운영 데이터를 잃어서는 안 됩니다."**

### 5.1. 금지 사항 (Forbidden Actions)
1.  **NO DROP**: 마이그레이션 스크립트(`upgrade` 함수) 안에 `op.drop_table`이 포함되어 있다면 **절대 승인 금지**입니다.
    *   예외: "Expand and Contract" 전략에 따라 데이터 이관이 100% 완료된 후, 더 이상 쓰이지 않는 테이블을 삭제하는 경우는 제외. (단, 이 경우에도 백업 필수)
2.  **Re-init 금지**: `drop_tables.py` 같은 초기화 스크립트는 로컬 개발 환경(`local`)이나 테스트(`test`) 환경에서만 사용해야 합니다. 운영(`prod`)에서는 절대 실행하지 마십시오.

### 5.2. 필수 절차 (Mandatory Procedures)
1.  **Backup First**: 운영 DB에 마이그레이션을 적용하기 전, 반드시 **스냅샷(Snapshot) 백업**을 생성해야 합니다.
2.  **Dry Run**: 실제 적용 전에 로컬 `staging` 환경에서 마이그레이션을 리허설하고 데이터 손실 여부를 확인하세요.

---

## 6. 데이터 복구 (Data Recovery)

혹시라도 초기화 등으로 데이터가 사라졌을 경우를 대비해, 기준 정보(Master Data)를 복구할 수 있는 시딩(Seeding) 스크립트를 관리해야 합니다.

- **스크립트 위치**: `scripts/seed_data.py` (예정)
- **사용법**: `uv run python scripts/seed_data.py`
