# Demo Runbook

## 목표

첫 번째 GitHub MCP 기반 에이전트 루프를 검증한다.

## 실행 순서

1. Demand Agent
   `issues/demo-issue-001.md` 내용을 기준으로 실제 GitHub Issue 생성

2. Research Agent
   `research/demo-issue-001-research.md` 내용을 이슈 코멘트 또는 브랜치 문서로 정리

3. Writer Agent
   `content/demo-issue-001-blog.md` 와 `content/demo-issue-001-channels.md`를 포함한 PR 생성

4. Safety Agent
   `reviews/demo-issue-001-safety-review.md` 기준으로 PR 검토

5. Chief Agent
   unresolved 리뷰 스레드 여부 확인 후 승인 또는 보류 판단

6. Distribution Agent
   승인 시 채널별 배포문 확정

## GitHub MCP 사용 예시

- 레포 확인: `_get_repo`
- PR 메타데이터 확인: `_get_pr_info`
- PR 전체 검토: `_fetch_pr`
- 리뷰 스레드 확인: `_list_pull_request_review_threads`
- 진행 코멘트 남기기: `_add_comment_to_issue`
- 리뷰 회신: `_reply_to_review_comment`

## 성공 기준

- 이슈 1개 생성
- PR 1개 생성
- 안전 검수 코멘트 반영
- 최종 발행 가능 판정까지 완료
