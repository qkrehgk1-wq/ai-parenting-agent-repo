# AI Parenting Agent Repo

이 저장소는 육아 AI 회사를 운영하기 위한 자동화된 AI 에이전트 팀의 기준 저장소다.

핵심 원칙은 단순하다.

- 모든 업무는 GitHub 이슈에서 시작한다.
- 모든 결과물은 브랜치와 Pull Request로 제출한다.
- 모든 품질 검토는 PR 코멘트와 리뷰 스레드에서 관리한다.
- 사람 창업자는 승인자이자 브랜드 책임자다.
- 최신 AI 흐름과 기능 변화는 주기적으로 점검하고 업그레이드한다.

## 1. 저장소의 역할

이 레포는 아래 6가지를 동시에 담당한다.

1. 콘텐츠 기획 보드
2. 리서치 자료 저장소
3. 에이전트 프롬프트 허브
4. 리뷰와 검수 기록 시스템
5. 자동화된 발행 파이프라인의 운영본부
6. 기능 업그레이드와 실험 백로그

## 2. 권장 GitHub MCP 활용 방식

이 팀은 GitHub MCP를 적극적으로 사용한다.

- `mcp__codex_apps__github._get_repo`
  레포 상태와 메타데이터 확인
- `mcp__codex_apps__github._fetch_pr`
  PR 전체 맥락과 변경 내용을 검토
- `mcp__codex_apps__github._get_pr_info`
  PR 제목, 설명, 상태, base/head 확인
- `mcp__codex_apps__github._list_pull_request_review_threads`
  unresolved 리뷰 스레드와 수정 포인트 확인
- `mcp__codex_apps__github._reply_to_review_comment`
  에이전트가 수정 결과를 리뷰 스레드에 회신
- `mcp__codex_apps__github._add_comment_to_issue`
  이슈 진행 상황, 리서치 요약, 다음 액션을 남김
- `mcp__codex_apps__github._compare_commits`
  초안 대비 개선량이나 변경 범위를 비교
- `mcp__codex_apps__github._fetch_commit`
  특정 커밋 단위로 품질과 변경 의도를 추적

## 3. 기본 운영 사이클

1. 수요 탐지 에이전트가 질문이나 트렌드를 바탕으로 GitHub Issue를 만든다.
2. 대표 에이전트가 이슈 우선순위를 정하고 라벨을 붙인다.
3. 리서치 에이전트가 근거 자료를 정리해 이슈 코멘트 또는 `research/` 문서로 남긴다.
4. 콘텐츠 에이전트가 별도 브랜치에서 초안을 작성한다.
5. 안전 검수 에이전트와 브랜드 검수 에이전트가 PR에서 리뷰한다.
6. 대표 에이전트가 최종 승인 후 배포 에이전트에 전달한다.
7. 배포 에이전트가 게시용 포맷을 생성하고 분석 에이전트가 성과를 기록한다.
8. 업그레이드 에이전트가 정기적으로 모델, 프롬프트, MCP 활용, 자동화 구조 개선안을 제안한다.

## 4. 디렉터리 개요

- `agents/`
  에이전트별 역할, 입력, 출력, GitHub 행동 규칙
- `issues/`
  이슈 템플릿과 운영 규칙
- `research/`
  주제별 조사 노트
- `content/`
  블로그, 카드뉴스, 뉴스레터 초안
- `reviews/`
  검수 기준과 체크리스트
- `ops/`
  일간 운영 리포트, KPI, 자동화 규칙

## 5. 시작 순서

1. 이 저장소를 GitHub에 올린다.
2. 이슈 템플릿과 라벨 체계를 만든다.
3. `agents/` 안의 프롬프트를 각 AI 에이전트의 시스템 역할로 등록한다.
4. 첫 번째 콘텐츠 이슈를 생성하고 PR 기반 생산 루프를 테스트한다.
5. 월간 `type:upgrade` 이슈를 열어 기능 개선 루프를 운영한다.

## 6. 추천 라벨 체계

- `source:demand`
- `source:trend`
- `type:content`
- `type:coaching`
- `type:product`
- `type:upgrade`
- `status:research`
- `status:draft`
- `status:review`
- `status:ready`
- `risk:medical`
- `risk:sensitive`
- `priority:high`
- `priority:normal`

## 7. 참고한 GitHub 레포 패턴

이번 설계에서 GitHub MCP로 확인한 대표적인 멀티에이전트 관련 공개 레포 메타데이터는 아래와 같다.

- `crewAIInc/crewAI`
- `langchain-ai/langgraph`
- `microsoft/autogen`

이 문서는 위 레포들의 세부 구현을 복제한 것이 아니라, 공개 레포 메타데이터를 바탕으로 "에이전트 분업", "상태 흐름", "검토 가능한 작업 단위"라는 운영 패턴을 우리 사업 구조에 맞게 재구성한 설계안이다.
