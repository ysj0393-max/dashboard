import streamlit as st
import json
from datetime import datetime
import pandas as pd

st.set_page_config(
    page_title="양승재님 Ralph Loop 대시보드",
    page_icon="🎯",
    layout="wide"
)

# CSS 스타일
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
    }
    .metric-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
    }
    .status-completed {
        color: #00cc00;
        font-weight: bold;
    }
    .status-progress {
        color: #ff9900;
        font-weight: bold;
    }
    .status-pending {
        color: #ff0000;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 헤더
st.markdown('<p class="main-header">🎯 양승재님 Ralph Loop 대시보드</p>', unsafe_allow_html=True)
st.markdown(f"*업데이트: {datetime.now().strftime('%Y-%m-%d %H:%M')} KST*")
st.markdown("---")

# 탭 생성
tab1, tab2, tab3, tab4 = st.tabs(["📊 태스크 현황", "📈 품질 추이", "🔄 컨텍스트 리셋", "⚙️ 시스템 상태"])

with tab1:
    st.subheader("오늘의 태스크")
    
    tasks = [
        {"name": "영어 스피킹", "status": "완료", "quality": 8, "time": "07:00"},
        {"name": "JD 크롤링", "status": "진행중", "quality": 6, "time": "09:00"},
        {"name": "LinkedIn 네트워킹", "status": "대기", "quality": 0, "time": "12:00"},
        {"name": "화요일 집중", "status": "대기", "quality": 0, "time": "18:00"},
        {"name": "멘탈 체크인", "status": "대기", "quality": 0, "time": "20:00"},
    ]
    
    for task in tasks:
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
        with col1:
            st.write(f"**{task['name']}**")
        with col2:
            if task['status'] == '완료':
                st.markdown('<span class="status-completed">🟢 완료</span>', unsafe_allow_html=True)
            elif task['status'] == '진행중':
                st.markdown('<span class="status-progress">🟡 진행중</span>', unsafe_allow_html=True)
            else:
                st.markdown('<span class="status-pending">🔴 대기</span>', unsafe_allow_html=True)
        with col3:
            st.write(f"품질: {task['quality']}/10")
        with col4:
            st.write(f"시간: {task['time']}")

with tab2:
    st.subheader("품질 추이")
    
    quality_data = {
        'JD 크롤링': [5, 6, 7, 8],
        '자소서 작성': [4, 5, 6],
        '영어 스피킹': [7, 7, 8, 8],
        '일일 결정 기록': [8, 8, 9, 9]
    }
    
    for task_name, scores in quality_data.items():
        col1, col2, col3 = st.columns([2, 3, 1])
        with col1:
            st.write(f"**{task_name}**")
        with col2:
            st.line_chart(scores, height=100)
        with col3:
            avg = sum(scores) / len(scores)
            st.write(f"평균: {avg:.1f}")

with tab3:
    st.subheader("컨텍스트 리셋 현황")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("마지막 리셋", "30분 전")
    with col2:
        st.metric("누적 리셋", "12회")
    with col3:
        st.metric("평균 복구 시간", "2분")
    
    st.markdown("---")
    st.info("💡 **팁:** 파일 기반 상태 관리로 컨텍스트 리셋에 강합니다.")

with tab4:
    st.subheader("시스템 상태")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("활성화된 cron", "17개")
        st.metric("평균 프롬프트 압축률", "60%")
    with col2:
        st.metric("다음 목표", "연봴 7,000만원+")
        st.metric("현재 단계", "gt30_lead")
    
    st.markdown("---")
    st.subheader("해시 태그 사전")
    
    hash_dict = {
        "[CTX:ysj_8y_ecom]": "양승재님, 8년, E-commerce",
        "[GOAL:gt30_lead]": "글로벌 탑30, Lead 포지션",
        "[TASK:jd_crawl]": "JD 크롤링",
        "[PLAT:li,jk]": "LinkedIn, JobKorea",
        "[FIL:7y,6k]": "7년+, 6천만원+"
    }
    
    for tag, meaning in hash_dict.items():
        st.code(f"{tag} = {meaning}")

# 푸터
st.markdown("---")
st.markdown("*Made with ❤️‍🔥 by Suhobot | Ralph Loop System v1.0*")
