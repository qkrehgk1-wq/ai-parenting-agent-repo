# PR Auto Summary Template

## 목적

이 템플릿은 GitHub MCP 기반으로 PR을 빠르게 읽기 위한 공통 출력 형식이다.
Chief Agent, Safety Agent, Upgrade Agent가 같은 프레임으로 PR을 해석하도록 돕는다.

## 사용 시점

- 대표 에이전트가 PR 우선순위를 판단할 때
- 안전 검수 에이전트가 전체 변경을 빠르게 파악할 때
- 업그레이드 팀이 운영 병목을 감지할 때

## 권장 입력

- `_get_pr_info`
- `_fetch_pr`
- `_list_pull_request_review_threads`

## 출력 형식

### 1. 기본 요약

- PR 제목:
- 관련 이슈:
- 현재 상태:
- base / head:

### 2. 핵심 변경

- 무엇이 바뀌었는지 3줄 이내 요약
- 주요 변경 파일:
- 사용자 또는 운영에 미치는 영향:

### 3. 검토 포인트

- 지금 가장 먼저 확인해야 할 부분:
- Safety Agent 확인 필요:
- Chief Agent 판단 필요:
- Upgrade Agent 관점의 개선 포인트:

### 4. 리뷰 병목

- unresolved 리뷰 스레드 수:
- 가장 중요한 막힘:
- 막힘 원인:
- 필요한 다음 액션:

### 5. 최종 판단 초안

- 지금 머지 가능한가:
- 보류 사유:
- 다음 담당 에이전트:

## 예시 출력

- PR 제목: feat: add upgrade team for recurring AI improvements
- 관련 이슈: demo-upgrade-001
- 현재 상태: review 필요
- base / head: main / feat/demo-content-safety-pass

- 핵심 변경: 업그레이드 팀 역할 문서, 업그레이드 이슈 템플릿, 운영 리듬 문서가 추가됨
- 주요 변경 파일: agents/upgrade-agent.md, .github/ISSUE_TEMPLATE/upgrade-request.yml, ops/upgrade-rhythm.md
- 사용자 또는 운영에 미치는 영향: 부모 노출 기능 변화는 없고 내부 운영 체계가 강화됨

- 지금 가장 먼저 확인해야 할 부분: 업그레이드 범위가 과도하지 않은지
- Safety Agent 확인 필요: 낮음
- Chief Agent 판단 필요: main 기준선에 포함할지
- Upgrade Agent 관점의 개선 포인트: 월간 실험 리포트 템플릿 추가 가능

- unresolved 리뷰 스레드 수: 0
- 가장 중요한 막힘: 없음
- 막힘 원인: 없음
- 필요한 다음 액션: PR 본문 보강 후 승인 가능

- 지금 머지 가능한가: 예
- 보류 사유: 없음
- 다음 담당 에이전트: Chief Agent
