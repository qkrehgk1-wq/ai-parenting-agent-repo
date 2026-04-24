# Labels Policy

## Source Labels

- `source:demand`
  부모 질문과 실제 수요에서 나온 이슈
- `source:trend`
  뉴스, 제도 변화, 시즌성 관심사에서 나온 이슈

## Type Labels

- `type:content`
  콘텐츠 제작 이슈
- `type:coaching`
  맞춤형 코칭 또는 상담형 응답 이슈
- `type:product`
  제품 추천, 비교, 제휴형 이슈

## Status Labels

- `status:research`
  조사 단계
- `status:draft`
  초안 작성 단계
- `status:review`
  리뷰 또는 검수 단계
- `status:ready`
  승인 직전 또는 배포 가능 상태

## Risk Labels

- `risk:medical`
  의료나 발달 관련 민감성이 높음
- `risk:sensitive`
  감정, 행동, 부모 불안 등 민감 표현 포함

## Priority Labels

- `priority:high`
  시급하게 처리할 필요가 있음
- `priority:normal`
  일반 우선순위

## Rules

- 민감도 `의료 민감` 이슈는 반드시 `risk:medical` 라벨 부착
- 리뷰 전 단계에서는 `status:draft` 유지
- unresolved 리뷰 스레드가 남아 있으면 `status:ready` 금지
- 배포 가능한 상태가 되면 `status:review`를 제거하고 `status:ready` 부착
