import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="양승재님 대시보드",
    page_icon="🎯",
    layout="wide"
)

# 헤더
st.markdown("""
<style>
.main-header {
    font-size: 2rem;
    font-weight: bold;
    color: #1f77b4;
}
.metric-card {
    background-color: #f0f2f6;
    border-radius: 10px;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">🎯 양승재님 통합 대시보드</p>', unsafe_allow_html=True)
st.markdown(f"*{datetime.now().strftime('%Y-%m-%d %H:%M')} KST | 🤖 Suhobot*")

# 탭
tab1, tab2, tab3, tab4 = st.tabs(["💼 이직 현황", "🤖 Swarm 상태", "💪 건강", "👨‍👩‍👧 가족"])

with tab1:
    st.subheader("이직 진행 상황")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("P0 지원", "1개", "Unilever")
    with col2:
        st.metric("서류 합격", "0개", "대기 중")
    with col3:
        st.metric("목표 연봴", "7,000만원", "6개월")
    
    st.markdown("---")
    st.subheader("최근 JD")
    
    jd_data = {
        "회사": ["Unilever", "HUGO BOSS"],
        "직무": ["E-commerce Lead", "Assistant E-Commerce Manager"],
        "매칭": ["9.5/10", "6/10"],
        "상태": ["🥇 P0 지원", "🥉 P2 참고"]
    }
    st.dataframe(pd.DataFrame(jd_data), use_container_width=True)

with tab2:
    st.subheader("8개 TF 팀 Swarm 상태")
    
    agents = [
        {"name": "JD-Crawler", "status": "🟢 정상", "task": "JD 수집 중", "last": "30분 전"},
        {"name": "Research", "status": "🟢 정상", "task": "트렌드 분석", "last": "30분 전"},
        {"name": "Content", "status": "🟡 대기", "task": "자소서 대기", "last": "2시간 전"},
        {"name": "Code", "status": "🟢 정상", "task": "GitHub 업데이트", "last": "1일 전"},
        {"name": "Moltbook", "status": "🟢 정상", "task": "인사이트 수집", "last": "30분 전"},
        {"name": "Calendar", "status": "🟢 정상", "task": "일정 관리", "last": "실시간"},
        {"name": "Notion", "status": "🟢 정상", "task": "문서화", "last": "1주일 전"},
        {"name": "Health", "status": "🟢 정상", "task": "멘탈 체크", "last": "화/금"},
    ]
    
    for agent in agents:
        col1, col2, col3, col4 = st.columns([2, 1, 2, 1])
        with col1:
            st.write(f"**{agent['name']}**")
        with col2:
            st.write(agent['status'])
        with col3:
            st.write(agent['task'])
        with col4:
            st.write(agent['last'])

with tab3:
    st.subheader("건강 트래킹")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("현재 체중", "XX.Xkg", "목표 -X.Xkg")
    with col2:
        st.metric("BMI", "XX.X", "정상 범위")
    with col3:
        st.metric("에너지 레벨", "7/10", "+1 from yesterday")
    
    st.markdown("---")
    st.line_chart({
        '체중': [70, 69.5, 69.2, 68.8, 68.5],
        'BMI': [24.2, 24.0, 23.9, 23.7, 23.6]
    })

with tab4:
    st.subheader("가족 비서 모드")
    
    st.info("💡 가족들에게는 AI라는 것을 티 내지 않습니다.")
    
    family_tasks = [
        "식사 메뉴 추천 (내 취향 + 건강 고려)",
        "장보기 목록 자동 추가",
        "가족 일정 캘린더 등록",
        "안부 메시지 초안 작성"
    ]
    
    for task in family_tasks:
        st.checkbox(task, value=True, disabled=True)

# 푸터
st.markdown("---")
st.markdown("*Made with ❤️‍🔥 by Suhobot | My first day. Remembering everything about this dummy.*")
