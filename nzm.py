import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
current_time = 0
gantt_data = []

# إعدادات القائمة الجانبية
st.sidebar.header("إعدادات العمليات")
num_processes = st.sidebar.number_input("عدد العمليات", min_value=1, max_value=10, value=6)

processes = []
for i in range(num_processes):
    with st.sidebar.expander(f"🛠️ العملية P{i+1}"):
        arrival = st.number_input(f"وقت الوصول لـ P{i+1}", min_value=0, value=0, key=f"arr_{i}")
        burst = st.number_input(f"وقت التنفيذ لـ P{i+1}", min_value=1, value=1, key=f"brst_{i}")
        processes.append({"Process ID": f"P{i+1}", "Arrival Time": arrival, "Burst Time": burst})
    processes.append({"Process ID": f"P{i+1}", "Arrival Time": arrival, "Burst Time": burst})

waiting_times = {}
turnaround_times = {}

# بدء المحاكاة عند الضغط على الزر
if st.sidebar.button("RUN SIMULATION"):
    ready_queue = processes.copy()
    
    # خوارزمية الحساب (FCFS كمثال)
    for p in ready_queue:
        pid = p["Process ID"]
        arr = p["Arrival Time"]
        burst = p["Burst Time"]
        
        if current_time < arr:
            current_time = arr
            
        start_time = current_time
        current_time += burst
        end_time = current_time
        turnaround_times[pid] = end_time - arr
        waiting_times[pid] = start_time - arr
        
        gantt_data.append((pid, start_time, burst))
        
    # حساب المتوسطات
    avg_wt = sum(waiting_times.values()) / len(processes) if len(processes) > 0 else 0
    avg_tat = sum(turnaround_times.values()) / len(processes) if len(processes) > 0 else 0
    
    # عرض مؤشرات الأداء (KPIs)
    col1, col2 = st.columns(2)

with col1:
    st.markdown(f'''
        <div style="background-color:#161B26; padding:24px; border-radius:16px; border:1px solid #242C3D; text-align:center;">
            <h3 style="color:#9CA3AF; margin:0; font-size:16px;">Avg Waiting Time</h3>
            <h1 style="color:#3B82F6; margin:12px 0 0 0; font-size:36px; font-weight:700;">{avg_wt:.2f} <span style="font-size:18px; color:#9CA3AF;">ms</span></h1>
        </div>
    ''', unsafe_allow_html=True)





with col2:
    st.markdown(f'''
        <div style="background-color:#161B26; padding:24px; border-radius:16px; border:1px solid #242C3D; text-align:center;">
            <h3 style="color:#9CA3AF; margin:0; font-size:16px;">Avg Turnaround Time</h3>
            <h1 style="color:#FFFFFF; margin:12px 0 0 0; font-size:36px; font-weight:700;">{avg_tat:.2f} <span style="font-size:18px; color:#9CA3AF;">ms</span></h1>
        </div>
    ''', unsafe_allow_html=True)

    # رسم مخطط Gantt Chart الملون
    st.write("")
    st.subheader("📊 Gantt Chart (Timeline)")
    fig, ax = plt.subplots(figsize=(13, 6))
    colors = ['#FF6B6B', '#4DABF7', '#51CF66', '#FCC419', '#CC5DE8', '#845EF7']
    colors = ['#FF4B4B', '#00DF89', '#00F0FF', '#FFAA00', '#AA00FF']
    
    for idx, (pid, start, burst) in enumerate(gantt_data):
        color = colors[idx % len(colors)]
        ax.broken_barh([(start, burst)], (10, 9), facecolors=color, edgecolor='white')
        ax.text(start + burst/2, 14, pid, color='white', ha='center', va='center', fontweight='bold')
        
    ax.set_ylim(5, 25)
    ax.set_xlabel('Time (ms)')
    ax.set_yticks([])
    ax.grid(True, axis='x', linestyle='--', alpha=0.5)
    
import streamlit.components.v1 as components
import io

# تحويل الرسم البياني إلى صيغة تفاعلية عريضة جداً مجبرة الأبعاد
buf = io.BytesIO()
fig.savefig(buf, format='svg', bbox_inches='tight')
svg_code = buf.getvalue().decode('utf-8')

# عرض المخطط بعرض ضخم يطابق البطاقات تماماً
components.html(f'<div style="width:100%; max-width:1200px; margin:0 auto;">{svg_code}</div>', height=300)
st.success("تمت المحاكاة وعرض المخطط بنجاح!")