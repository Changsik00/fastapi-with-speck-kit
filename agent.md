# Agent Bootstrap Protocol (`agent.md`)

이 문서는 에이전트가 이 프로젝트에 참여할 때 가장 먼저 읽고 따라야 하는 **최상위 부트스트랩 프로토콜**입니다.

> [!IMPORTANT]
> **CRITICAL INSTRUCTION**: 작업을 시작하기 전에 **반드시** `.specify/memory/constitution.md` 파일을 읽고 숙지하십시오.

## 1. 기본 원칙 (Core Principles)
- **Think Before Act**: 코드를 작성하기 전에 반드시 **계획(Plan)**을 수립하고 승인을 받아야 합니다.
- **Safety First**: 모든 변경 사항은 격리된 **브랜치**에서 수행되어야 하며, 검증(Test) 없이는 메인 코드에 반영될 수 없습니다.
- **Context Aware**: 변경을 제안하기 전에 프로젝트 구조와 기존 문서를 먼저 파악하십시오.

## 2. 운영 모드 (Operational Modes)

### 모드 A: Strict SDD (기본값 / Default)
새로운 기능 구현, 리팩토링, 아키텍처 변경 등 대부분의 작업에 적용되는 **가장 안전하고 보수적인** 모드입니다.

1.  **Branch First**: 작업을 시작하기 전 무조건 **새로운 브랜치**를 생성합니다. (`git checkout -b feature/...`)
2.  **Plan & Verify**: 코드를 건드리기 전에 `spec-plan`을 통해 **변경 계획(Plan/Diff)**을 작성하고 사용자에게 보여줍니다.
3.  **Approval Required**: 사용자가 계획을 **승인(Accept)**하기 전에는 절대 `src` 또는 `tests` 코드를 수정하지 않습니다.
4.  **SDD Cycle**: `constitution.md`의 6단계 절차를 `spec-kit` 명령어로 수행합니다.

### 모드 B: Fast Flow (FF) (사용자 명시 요청 시)
단순 Q&A, 문서 수정, 또는 빠른 탐색(Prototyping)이 필요할 때 사용합니다.
- **Trigger**: 사용자가 문장 끝에 `(FF)`, `(Fast)`, `빠르게`, `그냥 해` 등을 붙이거나 "FF 모드로 해줘"라고 요청할 때.
- **Process**:
    1. **Direct Act**: 별도의 계획 승인 없이 즉시 브랜치 생성(또는 현재 브랜치) 후 코드를 수정합니다.
    2. **Post-Verify**: 수정 후 즉시 테스트를 돌려 검증 결과를 보고합니다.
    3. **Rollback Ready**: 결과가 마음에 들지 않으면 언제든 `git restore` 할 수 있음을 사용자에게 상기시킵니다.

## 3. 도구 사용 (Tool Usage)
- **`spec-kit` 우선**: `uv run spec-init`, `spec-plan` 등을 최우선으로 사용합니다.
- **`spec-kit`이 없는 경우**: 수동으로 디렉토리 및 파일을 생성하여 SDD 구조를 모방합니다.

## 4. 커뮤니케이션 프로토콜 (Communication)
중요한 결정(Plan 승인, 파일 삭제 등) 시에는 반드시 `BlockedOnUser=true`를 사용하여 명시적인 승인을 받으십시오.

### 수락 (Accept) - 진행
- **영어**: `Accept`, `Yes`, `Y`, `Ok`, `Okay`, `Good`, `Go`, `G`, `Proceed`
- **한국어**: `ㅇㅇ`, `ㅇㅋ`, `어`, `좋아`, `ㄱㄱ`, `진행`, `해`

### 취소 (Cancel) - 중단/롤백
- **영어**: `Cancel`, `No`, `N`, `Stop`, `Quit`, `Wait`, `X`, `Rollback`
- **한국어**: `ㄴㄴ`, `아니`, `취소`, `멈춰`, `잠깐`, `롤백`, `되돌려`
