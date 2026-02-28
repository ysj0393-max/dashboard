#!/usr/bin/env python3
"""
양승재님 Ralph Loop 대시보드
실시간 태스크 상태 및 품질 모니터링
"""

import json
from datetime import datetime
from pathlib import Path

class RalphLoopDashboard:
    def __init__(self):
        self.tasks = {
            "jd_crawling": {
                "name": "JD 크롤링",
                "status": "🟢 완료",
                "quality": 8,
                "retries": 3,
                "next_run": "09:00",
                "last_run": "2026-02-28 09:00"
            },
            "english_speaking": {
                "name": "영어 스피킹", 
                "status": "🔴 대기",
                "quality": 0,
                "retries": 0,
                "next_run": "07:00",
                "last_run": None
            },
            "resume_writing": {
                "name": "자소서 작성",
                "status": "🟡 진행중",
                "quality": 6,
                "retries": 2,
                "next_run": None,
                "last_run": "2026-02-28 19:00"
            },
            "decision_log": {
                "name": "일일 결정 기록",
                "status": "🔴 대기",
                "quality": 0,
                "retries": 0,
                "next_run": "23:30",
                "last_run": None
            }
        }
        self.quality_trend = {
            "jd_crawling": [5, 6, 7, 8],
            "resume_writing": [4, 5, 6],
            "english_speaking": [7, 7, 8, 8],
            "decision_log": [8, 8, 9, 9]
        }
        self.reset_count = 12
        self.last_reset = "30분 전"
    
    def display(self):
        """대시보드 표시"""
        output = []
        output.append("=" * 50)
        output.append("🎯 양승재님 Ralph Loop 대시보드")
        output.append("=" * 50)
        output.append("")
        
        # 태스크 상태
        output.append("📊 태스크 상태")
        output.append("-" * 50)
        for task_id, task in self.tasks.items():
            status_line = f"{task['status']} {task['name']:<12} | 품질: {task['quality']}/10 | 반복: {task['retries']}회"
            if task['next_run']:
                status_line += f" | 다음: {task['next_run']}"
            output.append(status_line)
        
        output.append("")
        
        # 품질 추이
        output.append("📈 품질 추이")
        output.append("-" * 50)
        for task_id, scores in self.quality_trend.items():
            task_name = self.tasks[task_id]['name']
            trend = " → ".join(map(str, scores))
            avg = sum(scores) / len(scores)
            status = "상승중" if scores[-1] > scores[0] else "유지" if scores[-1] == scores[0] else "하락"
            output.append(f"{task_name:<12} | {trend} | 평균: {avg:.1f} | {status}")
        
        output.append("")
        
        # 컨텍스트 리셋
        output.append("🔄 컨텍스트 리셋")
        output.append("-" * 50)
        output.append(f"마지막 리셋: {self.last_reset}")
        output.append(f"누적 리셋: {self.reset_count}회")
        output.append(f"평균 복구 시간: 2분")
        
        output.append("")
        output.append("=" * 50)
        output.append(f"업데이트: {datetime.now().strftime('%H:%M:%S')}")
        output.append("=" * 50)
        
        return "\n".join(output)
    
    def update_task(self, task_id, **kwargs):
        """태스크 업데이트"""
        if task_id in self.tasks:
            self.tasks[task_id].update(kwargs)
            # 품질 추이 업데이트
            if 'quality' in kwargs:
                self.quality_trend[task_id].append(kwargs['quality'])
                # 최근 10개만 유지
                self.quality_trend[task_id] = self.quality_trend[task_id][-10:]
    
    def reset_context(self):
        """컨텍스트 리셋 기록"""
        self.reset_count += 1
        self.last_reset = "방금"
        # 파일 기반 상태로 복구
        return "컨텍스트 리셋 완료. 파일 상태에서 복구."

if __name__ == "__main__":
    dashboard = RalphLoopDashboard()
    print(dashboard.display())
