# Offer Production Runbook

## 목표

첫 상품 3종을 에이전트 팀이 실제로 생산하고 테스트할 수 있게 역할별 실행 순서를 정리한다.

## Offer 1. PDF 상품 생산 루프

1. Demand Agent
   많이 묻는 연령/주제를 찾는다

2. Research Agent
   주제별 근거 자료를 정리한다

3. Writer Agent
   PDF 본문 초안을 작성한다

4. Safety Agent
   위험 표현을 검수한다

5. Revenue Agent
   가격과 오퍼 구조를 검토한다

6. Distribution Agent
   판매 페이지용 요약 문안으로 변환한다

## Offer 2. 유료 뉴스레터 생산 루프

1. Growth Agent
   무료에서 유료 전환 CTA를 설계한다

2. Writer Agent
   무료판과 유료판 차이를 구조화한다

3. Revenue Agent
   가격과 유지 전략을 검토한다

4. Learning Agent
   오픈율, 클릭률, 전환률을 학습 포인트로 기록한다

## Offer 3. AI 코치 베타 생산 루프

1. Chief Agent
   베타 범위를 작게 제한한다

2. Coaching 계열 에이전트
   응답 구조를 설계한다

3. Safety Agent
   민감 응답 기준을 강화한다

4. Upgrade Agent
   프롬프트와 자동화 흐름을 개선한다

5. Revenue Agent
   신청 조건과 가격을 검토한다

## 원칙

- 처음부터 큰 상품을 만들지 않는다
- 작은 실험으로 검증한다
- 구매 데이터를 반드시 Learning Agent에 전달한다
