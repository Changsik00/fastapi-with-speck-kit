# Utility Scripts

이 디렉토리는 데이터베이스 관리, 검증 및 복구를 위한 유틸리티 스크립트를 포함하고 있습니다.
모든 스크립트는 프로젝트 루트에서 `uv run python scripts/<스크립트명>` 명령어로 실행해야 합니다.

## 📋 스크립트 목록

### 1. `seed_data.py` (데이터 복구/초기화)
- **용도**: 초기 데이터를 DB에 주입합니다. (Recovery 또는 초기 셋업용)
- **특징**: 데이터가 이미 존재하면 중복 생성을 방지하고 건너뜁니다(Idempotent).
- **실행**:
  ```bash
  PYTHONPATH=. uv run python scripts/seed_data.py
  ```

### 2. `verify_enforcement.py` (제약조건 검증)
- **용도**: DB의 제약조건(Restrictions)이 실제로 동작하는지 테스트합니다.
- **내용**:
    - `Apple!` (특수문자) 입력 시도 -> **실패(정상)** 확인
    - 51자 이상 이름 입력 시도 -> **실패(정상)** 확인
    - 정상 한글 데이터 입력 시도 -> **성공** 확인
- **실행**:
  ```bash
  PYTHONPATH=. uv run python scripts/verify_enforcement.py
  ```

### 3. `check_constraints.py` (메타데이터 확인)
- **용도**: PostgreSQL의 시스템 카탈로그(`pg_constraint`)를 조회하여, 테이블에 걸려 있는 실제 제약조건 쿼리문(DDL)을 출력합니다.
- **실행**:
  ```bash
  PYTHONPATH=. uv run python scripts/check_constraints.py
  ```

### 4. `check_data.py` (데이터 조회)
- **용도**: `item` 테이블의 데이터 개수와 샘플(상위 5개)을 조회합니다.
- **실행**:
  ```bash
  PYTHONPATH=. uv run python scripts/check_data.py
  ```

## ⚠️ 주의사항
- 이 스크립트들은 `PYTHONPATH=.` 설정이 필요할 수 있습니다 (모듈 import 경로 때문).
- 운영 환경(Production)에서 실행 시 `verify_enforcement.py` 같은 테스트 데이터 삽입 스크립트는 주의해서 사용하세요.
