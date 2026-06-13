#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OS2 - نظم التشغيل 2 العملي
Built by: Dr. Hassan Hegar - Mari Private University
بايثون خالص بدون أي مكتبات خارجية
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 7799

# ─── HTML كامل ───
HTML_CONTENT = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OS2 - نظم التشغيل 2 العملي</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');
* { margin: 0; padding: 0; box-sizing: border-box; }
/* ─── CSS VARIABLES: Dark & Light Mode ─── */
:root {
    --bg-body: #0f172a;
    --bg-card: rgba(30, 41, 59, 0.5);
    --bg-card-solid: rgba(30, 41, 59, 0.6);
    --bg-input: rgba(15, 23, 42, 0.8);
    --bg-sidebar: rgba(15, 23, 42, 0.98);
    --bg-header: rgba(15, 23, 42, 0.95);
    --text-primary: #f8fafc;
    --text-secondary: #e2e8f0;
    --text-muted: #94a3b8;
    --text-dim: #64748b;
    --accent: #22d3ee;
    --border-color: rgba(100, 116, 139, 0.2);
    --border-accent: rgba(34, 211, 238, 0.15);
}

body.light-mode {
    --bg-body: #f1f5f9;
    --bg-card: rgba(255, 255, 255, 0.7);
    --bg-card-solid: rgba(255, 255, 255, 0.9);
    --bg-input: #f8fafc;
    --bg-sidebar: rgba(255, 255, 255, 0.98);
    --bg-header: rgba(255, 255, 255, 0.95);
    --text-primary: #0f172a;
    --text-secondary: #1e293b;
    --text-muted: #475569;
    --text-dim: #64748b;
    --accent: #0891b2;
    --border-color: rgba(148, 163, 184, 0.3);
    --border-accent: rgba(8, 145, 178, 0.2);
}

body { font-family: 'Tajawal', sans-serif; background: var(--bg-body); color: var(--text-secondary); min-height: 100vh; transition: background 0.3s, color 0.3s; }
a { text-decoration: none; color: inherit; }

.header {
    background: var(--bg-header);
    border-bottom: 1px solid var(--border-accent);
    padding: 12px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 1000;
    transition: background 0.3s, border 0.3s;
}
.header-left { display: flex; align-items: center; gap: 12px; }
.logo-icon { width: 36px; height: 36px; background: rgba(34, 211, 238, 0.1); border: 1px solid rgba(34, 211, 238, 0.3); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; }
.header-title { font-size: 1rem; font-weight: 700; color: var(--text-primary); transition: color 0.3s; }
.header-sub { font-size: 0.7rem; color: var(--text-muted); transition: color 0.3s; }
.section-badge { padding: 4px 12px; background: rgba(34, 211, 238, 0.1); border: 1px solid rgba(34, 211, 238, 0.2); border-radius: 20px; font-size: 0.75rem; color: #22d3ee; }
body.light-mode .section-badge { color: #0891b2; background: rgba(8, 145, 178, 0.1); border-color: rgba(8, 145, 178, 0.2); }

.container { display: flex; margin-top: 61px; min-height: calc(100vh - 61px); }
.sidebar { width: 260px; background: var(--bg-sidebar); border-left: 1px solid var(--border-accent); padding: 16px; overflow-y: auto; position: fixed; right: 0; top: 61px; bottom: 0; z-index: 100; transition: background 0.3s, border 0.3s, right 0.3s; }
.sidebar-section-title { font-size: 0.65rem; color: var(--text-dim); text-transform: uppercase; letter-spacing: 1px; margin: 16px 0 8px; padding: 0 8px; transition: color 0.3s; }
.nav-btn { display: flex; align-items: center; gap: 10px; padding: 8px 12px; border-radius: 8px; font-size: 0.85rem; color: var(--text-muted); transition: all 0.2s; margin: 2px 0; border: none; background: none; width: 100%; cursor: pointer; font-family: 'Tajawal', sans-serif; }
.nav-btn:hover { background: rgba(34, 211, 238, 0.08); color: var(--text-secondary); }
body.light-mode .nav-btn:hover { background: rgba(8, 145, 178, 0.08); }
.nav-btn.active { background: rgba(34, 211, 238, 0.12); color: #22d3ee; font-weight: 600; }
body.light-mode .nav-btn.active { color: #0891b2; background: rgba(8, 145, 178, 0.12); }
.main { flex: 1; margin-right: 260px; padding: 24px 32px; max-width: calc(100% - 260px); }

.hero { text-align: center; padding: 40px 20px; background: var(--bg-card); border: 1px solid var(--border-accent); border-radius: 16px; margin-bottom: 24px; transition: background 0.3s, border 0.3s; }
.hero h1 { font-size: 2rem; color: #22d3ee; font-weight: 800; margin-bottom: 8px; }
body.light-mode .hero h1 { color: #0891b2; }
.hero p { color: var(--text-muted); font-size: 0.9rem; max-width: 500px; margin: 0 auto 12px; transition: color 0.3s; }

.kpi-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 32px; }
.kpi-card { background: var(--bg-card-solid); border: 1px solid var(--border-accent); border-radius: 12px; padding: 20px; text-align: center; transition: background 0.3s, border 0.3s; }
.kpi-icon { font-size: 1.5rem; margin-bottom: 8px; }
.kpi-value { font-size: 1.8rem; font-weight: 800; color: #22d3ee; }
body.light-mode .kpi-value { color: #0891b2; }
.kpi-label { font-size: 0.75rem; color: var(--text-muted); margin-top: 4px; transition: color 0.3s; }

.section-title { display: flex; align-items: center; gap: 8px; color: #22d3ee; font-size: 1.1rem; font-weight: 700; margin: 24px 0 16px; }
body.light-mode .section-title { color: #0891b2; }
.section-count { margin-right: auto; font-size: 0.75rem; color: var(--text-dim); font-weight: 400; transition: color 0.3s; }

.cards-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-bottom: 24px; }
.card { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 16px; transition: all 0.3s; cursor: pointer; }
.card:hover { border-color: var(--border-accent); transform: translateY(-2px); }
.card-title { color: var(--text-primary); font-weight: 600; font-size: 0.95rem; margin-bottom: 4px; transition: color 0.3s; }
.card-desc { color: var(--text-muted); font-size: 0.8rem; line-height: 1.6; transition: color 0.3s; }

.projects-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 24px; }
.project-card { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: all 0.3s; cursor: pointer; }
.project-card:hover { border-color: var(--border-accent); transform: translateY(-2px); }
.project-icon { font-size: 2rem; margin-bottom: 8px; }
.project-title { color: var(--text-primary); font-weight: 700; font-size: 0.95rem; margin-bottom: 4px; transition: color 0.3s; }
.project-desc { color: var(--text-muted); font-size: 0.78rem; line-height: 1.5; transition: color 0.3s; }

.page-title { display: flex; align-items: center; gap: 10px; font-size: 1.3rem; color: #22d3ee; font-weight: 700; margin-bottom: 16px; }
.page-desc { color: #94a3b8; font-size: 0.9rem; line-height: 1.7; margin-bottom: 20px; }

.sim-box { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; margin-bottom: 16px; transition: background 0.3s, border 0.3s; }
.sim-row { display: flex; align-items: center; gap: 12px; padding: 10px; background: var(--bg-input); border-radius: 8px; margin: 6px 0; transition: background 0.3s; }
.sim-status { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }
.sim-status.running { background: #22d3ee; box-shadow: 0 0 8px #22d3ee; }
.sim-status.done { background: #10b981; }
.sim-status.waiting { background: #475569; }
body.light-mode .sim-status.waiting { background: #cbd5e1; }
.sim-label { font-size: 0.85rem; color: var(--text-secondary); transition: color 0.3s; }

.code-block { background: #0d1117; border: 1px solid #30363d; border-radius: 10px; padding: 16px; font-family: 'Courier New', monospace; font-size: 0.8rem; color: #e6edf3; overflow-x: auto; direction: ltr; text-align: left; line-height: 1.8; margin: 12px 0; }
body.light-mode .code-block { background: #f1f5f9; border-color: #e2e8f0; color: #1e293b; }
.info-box { background: rgba(34, 211, 238, 0.08); border: 1px solid rgba(34, 211, 238, 0.2); border-radius: 10px; padding: 14px; color: var(--text-muted); font-size: 0.85rem; line-height: 1.7; margin: 12px 0; transition: all 0.3s; }
body.light-mode .info-box { background: rgba(8, 145, 178, 0.06); border-color: rgba(8, 145, 178, 0.15); }

.gantt-container { background: rgba(15, 23, 42, 0.6); border-radius: 12px; padding: 16px; margin: 16px 0; transition: background 0.3s; }
body.light-mode .gantt-container { background: rgba(255, 255, 255, 0.5); }
.gantt-track { width: 100%; height: 30px; background: rgba(30, 41, 59, 0.8); border-radius: 6px; position: relative; overflow: hidden; margin: 8px 0; transition: background 0.3s; }
body.light-mode .gantt-track { background: rgba(203, 213, 225, 0.5); }
.gantt-block { position: absolute; height: 100%; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700; color: white; }

.process-config { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin: 16px 0; }
.process-card { background: var(--bg-card-solid); border: 1px solid var(--border-accent); border-radius: 10px; padding: 12px; text-align: center; transition: background 0.3s, border 0.3s; }
.process-input { width: 100%; padding: 6px; background: var(--bg-input); border: 1px solid var(--border-color); border-radius: 6px; color: var(--text-secondary); text-align: center; font-family: 'Tajawal', sans-serif; margin: 4px 0; transition: all 0.3s; }

.kpi-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin: 16px 0; }
.thread-bar-track { width: 100%; height: 8px; background: #1e293b; border-radius: 4px; overflow: hidden; margin: 4px 0; }
.thread-bar-fill { height: 100%; border-radius: 4px; transition: width 0.5s; }

.counter-display { text-align: center; padding: 30px; background: rgba(15, 23, 42, 0.6); border-radius: 16px; border: 1px solid rgba(34, 211, 238, 0.2); margin: 16px 0; }
.counter-value { font-size: 3.5rem; font-weight: 800; color: #22d3ee; }

.thread-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin: 16px 0; }
.thread-circle { text-align: center; padding: 12px; border-radius: 10px; border: 2px solid #334155; background: rgba(30, 41, 59, 0.5); transition: all 0.3s; }
.thread-circle.active { border-color: #22d3ee; background: rgba(34, 211, 238, 0.1); }
.thread-circle.done { border-color: #10b981; background: rgba(16, 185, 129, 0.1); }
.thread-dot { width: 24px; height: 24px; border-radius: 50%; margin: 0 auto 6px; }
.thread-name { font-size: 0.7rem; color: #94a3b8; }

.printer-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin: 16px 0; }
.printer-box { text-align: center; padding: 14px; border-radius: 10px; border: 2px solid #334155; background: rgba(30, 41, 59, 0.5); transition: all 0.3s; }
.printer-box.busy { border-color: #22d3ee; }

.deadlock-process { display: flex; align-items: center; gap: 12px; padding: 12px; background: rgba(30, 41, 59, 0.5); border-radius: 10px; margin: 6px 0; }
.process-badge { width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; font-size: 0.8rem; flex-shrink: 0; background: #475569; transition: all 0.3s; }
.process-badge.waiting { background: #ef4444; }
.process-badge.safe { background: #22d3ee; }

.chart-container { background: rgba(30, 41, 59, 0.4); border-radius: 12px; padding: 16px; margin: 12px 0; transition: background 0.3s; }
body.light-mode .chart-container { background: rgba(255, 255, 255, 0.5); }
.chart-bar { display: flex; align-items: center; margin: 8px 0; }
.chart-label { width: 100px; font-size: 0.8rem; color: var(--text-muted); transition: color 0.3s; }
.chart-track { flex: 1; height: 24px; background: rgba(30, 41, 59, 0.8); border-radius: 6px; overflow: hidden; position: relative; transition: background 0.3s; }
body.light-mode .chart-track { background: rgba(203, 213, 225, 0.5); }
.chart-fill { height: 100%; border-radius: 6px; display: flex; align-items: center; padding: 0 8px; color: white; font-size: 0.75rem; font-weight: 600; }

.data-table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 0.85rem; }
.data-table th { background: rgba(30, 41, 59, 0.8); padding: 10px; text-align: center; color: #22d3ee; font-weight: 600; border-bottom: 1px solid rgba(34, 211, 238, 0.2); transition: all 0.3s; }
body.light-mode .data-table th { background: rgba(241, 245, 249, 0.9); color: #0891b2; border-bottom-color: rgba(8, 145, 178, 0.2); }
.data-table td { padding: 10px; text-align: center; border-bottom: 1px solid rgba(100, 116, 139, 0.1); color: var(--text-secondary); transition: all 0.3s; }
body.light-mode .data-table td { border-bottom-color: rgba(148, 163, 184, 0.2); }
.data-table tr:hover td { background: rgba(30, 41, 59, 0.3); }
body.light-mode .data-table tr:hover td { background: rgba(241, 245, 249, 0.5); }

.railway-viz { position: relative; height: 160px; background: rgba(15, 23, 42, 0.6); border-radius: 12px; overflow: hidden; margin: 16px 0; }
.railway-road { position: absolute; top: 55%; left: 0; right: 0; height: 40px; background: rgba(51, 65, 85, 0.5); }
.railway-track { position: absolute; top: 15%; left: 0; right: 0; height: 50px; }
.rail-track-line { height: 6px; background: #8B6914; margin: 3px 0; }

.server-status { padding: 16px; background: rgba(15, 23, 42, 0.8); border-radius: 12px; border: 1px solid rgba(34, 211, 238, 0.2); margin: 16px 0; transition: all 0.3s; }
body.light-mode .server-status { background: rgba(255, 255, 255, 0.7); border-color: rgba(8, 145, 178, 0.15); }
.server-bar { width: 100%; height: 8px; background: #1e293b; border-radius: 4px; overflow: hidden; transition: background 0.3s; }
body.light-mode .server-bar { background: #cbd5e1; }
.server-bar-fill { height: 100%; background: #10b981; border-radius: 4px; transition: width 0.5s; }

.btn {
    display: inline-block;
    padding: 10px 24px;
    background: rgba(34, 211, 238, 0.15);
    border: 1px solid rgba(34, 211, 238, 0.3);
    border-radius: 10px;
    color: #22d3ee;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
    font-family: 'Tajawal', sans-serif;
    font-size: 0.9rem;
}
.btn:hover { background: rgba(34, 211, 238, 0.25); transform: scale(1.02); }

.page { display: none; }
.page.active { display: block; }

/* ─── MOBILE SIDEBAR DRAWER ─── */
.menu-btn { display: none; }
.sidebar-overlay { display: none; }
.bottom-nav { display: none; }

@media (max-width: 768px) {
    .menu-btn { display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; background: rgba(34, 211, 238, 0.1); border: 1px solid rgba(34, 211, 238, 0.3); border-radius: 8px; color: #22d3ee; font-size: 1.3rem; cursor: pointer; font-family: 'Tajawal', sans-serif; }
    .sidebar { display: block; right: -260px; transition: right 0.3s; z-index: 200; }
    .sidebar.open { right: 0; }
    .sidebar-overlay { display: block; position: fixed; inset: 0; background: rgba(0,0,0,0.6); z-index: 150; opacity: 0; visibility: hidden; transition: all 0.3s; }
    .sidebar-overlay.show { opacity: 1; visibility: visible; }
    .main { margin-right: 0; max-width: 100%; padding: 16px; padding-bottom: 70px; }
    .kpi-grid { grid-template-columns: repeat(2, 1fr); }
    .cards-grid { grid-template-columns: 1fr; }
    .projects-grid { grid-template-columns: 1fr; }
    .process-config { grid-template-columns: repeat(2, 1fr); }
    .bottom-nav { display: flex; position: fixed; bottom: 0; left: 0; right: 0; background: var(--bg-sidebar); border-top: 1px solid var(--border-accent); z-index: 100; justify-content: center; padding: 8px 0; transition: background 0.3s, border 0.3s; }
    .bottom-nav-item { display: flex; flex-direction: column; align-items: center; gap: 2px; padding: 6px 20px; border-radius: 8px; color: var(--text-muted); font-size: 0.7rem; cursor: pointer; transition: all 0.2s; border: 1px solid var(--border-color); background: var(--bg-card); font-family: 'Tajawal', sans-serif; }
    .bottom-nav-item:hover { color: var(--accent); background: var(--bg-card-solid); border-color: var(--border-accent); }
    .bottom-nav-item span { font-size: 1.3rem; }
}

/* ─── ANIMATIONS ─── */
@keyframes trainPass {
    0% { left: -20%; }
    100% { left: 120%; }
}
@keyframes carMoveLeft {
    0% { left: 85%; }
    100% { left: 10%; }
}
@keyframes carMoveRight {
    0% { left: 5%; }
    100% { left: 80%; }
}
@keyframes droneFly1 {
    0% { left: 20%; top: 20%; }
    25% { left: 30%; top: 15%; }
    50% { left: 45%; top: 25%; }
    75% { left: 55%; top: 20%; }
    100% { left: 70%; top: 25%; }
}
@keyframes droneFly2 {
    0% { left: 60%; top: 40%; }
    25% { left: 50%; top: 35%; }
    50% { left: 40%; top: 45%; }
    75% { left: 30%; top: 40%; }
    100% { left: 20%; top: 45%; }
}
@keyframes droneFly3 {
    0% { left: 30%; top: 60%; }
    25% { left: 40%; top: 55%; }
    50% { left: 50%; top: 65%; }
    75% { left: 60%; top: 55%; }
    100% { left: 70%; top: 60%; }
}
@keyframes blinkRed {
    0%, 100% { opacity: 1; background: #ef4444; }
    50% { opacity: 0.3; background: #7f1d1d; }
}
@keyframes barrierClose {
    0% { height: 8px; background: #10b981; }
    100% { height: 40px; background: #ef4444; }
}
@keyframes barrierOpen {
    0% { height: 40px; background: #ef4444; }
    100% { height: 8px; background: #10b981; }
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}
@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-5px); }
}
@keyframes trafficCarNorth {
    0% { top: -10%; opacity: 0; }
    20% { opacity: 1; }
    80% { opacity: 1; }
    100% { top: 90%; opacity: 0; }
}
@keyframes trafficCarSouth {
    0% { bottom: -10%; opacity: 0; }
    20% { opacity: 1; }
    80% { opacity: 1; }
    100% { bottom: 90%; opacity: 0; }
}
@keyframes trafficCarEast {
    0% { right: -10%; opacity: 0; }
    20% { opacity: 1; }
    80% { opacity: 1; }
    100% { right: 90%; opacity: 0; }
}
@keyframes trafficCarWest {
    0% { left: -10%; opacity: 0; }
    20% { opacity: 1; }
    80% { opacity: 1; }
    100% { left: 90%; opacity: 0; }
}
.animate-fade-in { animation: fadeInUp 0.4s ease-out; }
.animate-pulse { animation: pulse 1s ease-in-out infinite; }
.animate-float { animation: float 3s ease-in-out infinite; }

/* ─── RAILWAY ENHANCED ─── */
.train-elem { position: absolute; font-size: 2.5rem; left: -20%; top: 12%; z-index: 5; transition: none; }
.train-moving { animation: trainPass 3s linear forwards; }
.car-elem { position: absolute; font-size: 1.3rem; z-index: 4; }
.car-moving-left { animation: carMoveLeft 2.5s linear forwards; }
.car-moving-right { animation: carMoveRight 2.5s linear forwards; }
.barrier-elem { position: absolute; top: 35%; width: 5px; border-radius: 3px; transform-origin: top; transition: all 0.8s ease; }
.barrier-left { left: 32%; }
.barrier-right { left: 68%; }
.warn-light { position: absolute; top: 28%; left: 50%; transform: translateX(-50%); width: 14px; height: 14px; border-radius: 50%; background: #334155; z-index: 10; transition: background 0.3s; }
.warn-light.on { animation: blinkRed 0.6s infinite; background: #ef4444; }

/* ─── DRONE ENHANCED ─── */
.drone-scene { position: relative; height: 180px; background: rgba(15,23,42,0.6); border-radius: 12px; overflow: hidden; margin: 16px 0; }
.drone-zone { position: absolute; left: 40%; top: 30%; width: 20%; height: 28%; border: 2px dashed #f59e0b; border-radius: 8px; background: rgba(245,158,11,0.05); display: flex; align-items: center; justify-content: center; font-size: 0.6rem; color: #f59e0b; z-index: 2; transition: all 0.5s; }
.drone-zone.locked { border-color: #ef4444; background: rgba(239,68,68,0.1); color: #ef4444; }
.drone-elem { position: absolute; font-size: 1.8rem; z-index: 5; transition: all 0.8s cubic-bezier(0.4,0,0.2,1); filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3)); }
.drone-fly-1 { animation: droneFly1 4s ease-in-out infinite; }
.drone-fly-2 { animation: droneFly2 5s ease-in-out infinite; }
.drone-fly-3 { animation: droneFly3 4.5s ease-in-out infinite; }

/* ─── TRAFFIC ENHANCED ─── */
.traffic-scene { position: relative; height: 220px; background: rgba(15,23,42,0.6); border-radius: 12px; overflow: hidden; margin: 16px 0; }
.traffic-road-h { position: absolute; top: 50%; left: 0; right: 0; height: 50px; background: rgba(51,65,85,0.6); transform: translateY(-50%); }
.traffic-road-v { position: absolute; left: 50%; top: 0; bottom: 0; width: 50px; background: rgba(51,65,85,0.6); transform: translateX(-50%); }
.traffic-intersection { position: absolute; top: 50%; left: 50%; width: 50px; height: 50px; background: rgba(71,85,105,0.7); transform: translate(-50%,-50%); border: 2px solid rgba(100,116,139,0.3); border-radius: 4px; z-index: 3; }
.tl { position: absolute; width: 12px; height: 12px; border-radius: 50%; z-index: 10; transition: background 0.3s; }
.tl-n { top: 42%; left: 48%; }
.tl-s { bottom: 42%; left: 50%; }
.tl-e { top: 48%; right: 42%; }
.tl-w { top: 50%; left: 42%; }
.tcar { position: absolute; font-size: 1.2rem; z-index: 5; opacity: 0; }
.tcar-go-n { animation: trafficCarNorth 2s linear forwards; }
.tcar-go-s { animation: trafficCarSouth 2s linear forwards; }
.tcar-go-e { animation: trafficCarEast 2s linear forwards; }
.tcar-go-w { animation: trafficCarWest 2s linear forwards; }

</style>
</head>
<body>
    <div class="header">
        <div class="header-left">
            <button class="menu-btn" onclick="toggleSidebar()">☰</button>
            <div class="logo-icon">🖥️</div>
            <div>
                <div class="header-title">نظم التشغيل 2 - العملي</div>
                <div class="header-sub">د.حسن حجار - جامعة ماري الخاصة</div>
            </div>
        </div>
        <div class="header-right">
            <span class="section-badge">13 قسم</span>
        </div>
    </div>
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>
    <div class="container">
        <div class="sidebar" id="sidebar">
            <div class="sidebar-section-title">📚 المفاهيم النظرية (6)</div>
            <button class="nav-btn active" onclick="showPage('home'); closeSidebar();">🏠 الرئيسية</button>
            <button class="nav-btn" onclick="showPage('sequential'); closeSidebar();">📝 التنفيذ المتسلسل</button>
            <button class="nav-btn" onclick="showPage('threads'); closeSidebar();">🔀 الخيوط (Threads)</button>
            <button class="nav-btn" onclick="showPage('race'); closeSidebar();">⚠️ Race Condition</button>
            <button class="nav-btn" onclick="showPage('mutex'); closeSidebar();">🔒 Mutex Lock</button>
            <button class="nav-btn" onclick="showPage('deadlock'); closeSidebar();">🛑 Deadlock</button>
            <div class="sidebar-section-title">🛠️ المشاريع العملية (7)</div>
            <button class="nav-btn" onclick="showPage('cpu'); closeSidebar();">🧮 CPU Scheduler</button>
            <button class="nav-btn" onclick="showPage('atm'); closeSidebar();">🏧 ATM Machine</button>
            <button class="nav-btn" onclick="showPage('railway'); closeSidebar();">🚂 Railway Crossing</button>
            <button class="nav-btn" onclick="showPage('traffic'); closeSidebar();">🚗 Smart Traffic AI</button>
            <button class="nav-btn" onclick="showPage('drone'); closeSidebar();">🚁 Drone Coordination</button>
            <button class="nav-btn" onclick="showPage('game'); closeSidebar();">🎮 Game Server</button>
            <button class="nav-btn" onclick="showPage('printer'); closeSidebar();">🖨️ إدارة الموارد</button>
            <div class="sidebar-section-title">📊 الإحصائيات</div>
            <button class="nav-btn" onclick="showPage('dashboard'); closeSidebar();">📊 لوحة المراقبة</button>
        </div>
        <div class="main" id="main-content">
            <!-- Pages will be inserted here -->
        </div>
    </div>
    <div class="bottom-nav">
        <button class="bottom-nav-item" onclick="toggleDarkMode()" id="darkModeBtn"><span id="darkModeIcon">☀️</span><span id="darkModeLabel">Bright Mode</span></button>
    </div>

<script>
// ─── PAGE DATA ───
const PAGES = {};

// ─── HOME ───
PAGES.home = `
    <div class="hero">
        <div style="font-size:3rem;margin-bottom:12px;">🖥️</div>
        <h1>نظم التشغيل 2 - العملي</h1>
        <p>منصة تعليمية تفاعلية لمادة نظم التشغيل 2 العملي. تضم 6 مفاهيم نظرية + 7 مشاريع عملية + لوحة مراقبة شاملة.</p>
        <div style="color:#64748b;font-size:0.8rem;">👨‍🏫 <span style="color:#22d3ee;">د.حسن حجار</span> | جامعة ماري الخاصة</div>
    </div>
    <div class="kpi-grid">
        <div class="kpi-card"><div class="kpi-icon">📖</div><div class="kpi-value">6</div><div class="kpi-label">مفاهيم نظرية</div></div>
        <div class="kpi-card"><div class="kpi-icon">⚙️</div><div class="kpi-value">7</div><div class="kpi-label">مشاريع عملية</div></div>
        <div class="kpi-card"><div class="kpi-icon">⚡</div><div class="kpi-value">3+</div><div class="kpi-label">خوارزميات</div></div>
        <div class="kpi-card"><div class="kpi-icon">📊</div><div class="kpi-value">1</div><div class="kpi-label">لوحة مراقبة</div></div>
    </div>
    <div class="section-title"><span>📖</span><span>المفاهيم النظرية</span><span class="section-count">6 أقسام</span></div>
    <div class="cards-grid">
        <div class="card" onclick="showPage('sequential')"><div class="card-title">📝 التنفيذ المتسلسل</div><div class="card-desc">تنفيذ المهام واحدة تلو الأخرى بشكل متسلسل</div></div>
        <div class="card" onclick="showPage('threads')"><div class="card-title">🔀 الخيوط (Threads)</div><div class="card-desc">وحدات تنفيذ خفيفة ضمن نفس العملية</div></div>
        <div class="card" onclick="showPage('race')"><div class="card-title">⚠️ Race Condition</div><div class="card-desc">يتنافس عدة Threads على نفس المورد</div></div>
        <div class="card" onclick="showPage('mutex')"><div class="card-title">🔒 Mutex Lock</div><div class="card-desc">يمنع دخول أكثر من Thread للـ Critical Section</div></div>
        <div class="card" onclick="showPage('deadlock')"><div class="card-title">🛑 Deadlock</div><div class="card-desc">الجموس عندما تنتظر العمليات بعضها البعض</div></div>
    </div>
    <div class="section-title"><span>⚙️</span><span>المشاريع العملية</span><span class="section-count">7 مشاريع</span></div>
    <div class="projects-grid">
        <div class="project-card" onclick="showPage('cpu')"><div class="project-icon">🧮</div><div class="project-title">CPU Scheduler Simulator</div><div class="project-desc">يدعم FCFS و SJF و Round Robin مع مخطط Gantt</div></div>
        <div class="project-card" onclick="showPage('atm')"><div class="project-icon">🏧</div><div class="project-title">ATM Machine</div><div class="project-desc">محاكاة ATM: كل عميل Thread + Lock للرصيد</div></div>
        <div class="project-card" onclick="showPage('railway')"><div class="project-icon">🚂</div><div class="project-title">Railway Crossing</div><div class="project-desc">قطار + سيارات + Barrier يستخدم Mutex</div></div>
        <div class="project-card" onclick="showPage('traffic')"><div class="project-icon">🚗</div><div class="project-title">Smart Traffic AI</div><div class="project-desc">تقاطع طرق ذكي لمنع Gridlock</div></div>
        <div class="project-card" onclick="showPage('printer')"><div class="project-icon">🖨️</div><div class="project-title">إدارة الموارد (Printer)</div><div class="project-desc">3 طابعات و 6 مستخدمين باستخدام Semaphore</div></div>
        <div class="project-card" onclick="showPage('drone')"><div class="project-icon">🚁</div><div class="project-title">Drone Coordination</div><div class="project-desc">تنسيق طائرات بدون طيار + Mutex</div></div>
        <div class="project-card" onclick="showPage('game')"><div class="project-icon">🎮</div><div class="project-title">Game Server</div><div class="project-desc">خادم لعبة متعدد اللاعبين + Mutex Scoreboard</div></div>
    </div>
`;

// ─── SEQUENTIAL ───
PAGES.sequential = `
    <div class="page-title">📝 التنفيذ المتسلسل (Sequential Execution)</div>
    <div class="page-desc">في التنفيذ المتسلسل، تُنفذ المهام واحدة تلو الأخرى. كل مهمة يجب أن تنتهي قبل بدء المهمة التالية.</div>
    <div class="sim-box">
        <div style="display:flex;gap:10px;margin-bottom:16px;">
            <button class="btn" onclick="runSequential()">▶️ تشغيل المحاكاة</button>
            <button class="btn" onclick="resetSequential()">🔄 إعادة</button>
        </div>
        ${[0,1,2,3,4].map(i => `<div class="sim-row seq-task" id="seq-${i}"><span class="sim-status waiting"></span><span class="sim-label">Task ${i} ⏳ ينتظر</span></div>`).join('')}
        <div id="seq-result" class="info-box" style="display:none;margin-top:12px;">✅ انتهى! المدة: ~5 ثواني</div>
    </div>
    <div class="code-block">import time<br><br>print("Start Program")<br>for i in range(5):<br>&nbsp;&nbsp;&nbsp;&nbsp;print(f"Task {i} is running")<br>&nbsp;&nbsp;&nbsp;&nbsp;time.sleep(1)<br>print("End Program")</div>
    <div class="info-box">📌 <strong>ملخص التنفيذ المتسلسل</strong><br>• كل مهمة تنتظر انتهاء السابقة<br>• المدة الكلية = مجموع المدد<br>• لا يوجد Concurrency</div>
`;

// ─── THREADS ───
PAGES.threads = `
    <div class="page-title">🔀 الخيوط (Threads)</div>
    <div class="page-desc">الخيوط (Threads) هي وحدات تنفيذ خفيفة ضمن نفس العملية. تتيح تنفيذ مهام متعددة بشكل متزامن.</div>
    <div class="sim-box">
        <div style="display:flex;gap:10px;margin-bottom:16px;">
            <button class="btn" onclick="runThreads()">▶️ تشغيل</button>
            <button class="btn" onclick="resetThreads()">🔄 إعادة</button>
        </div>
        ${['#22d3ee','#a78bfa','#f472b6'].map((c,i) => `
            <div style="margin:8px 0;">
                <div style="display:flex;justify-content:space-between;font-size:0.8rem;color:#94a3b8;margin-bottom:4px;">
                    <span style="color:${c};">● Thread ${i+1}</span><span id="thread-status-${i}">Idle</span>
                </div>
                <div class="thread-bar-track"><div class="thread-bar-fill" id="thread-fill-${i}" style="width:0%;background:${c};"></div></div>
            </div>
        `).join('')}
    </div>
    <div class="code-block">import threading, time<br><br>def task(name):<br>&nbsp;&nbsp;&nbsp;&nbsp;for i in range(3):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(f"{name} - iteration {i}")<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time.sleep(0.5)<br><br>t1 = threading.Thread(target=task, args=("Thread 1",))<br>t2 = threading.Thread(target=task, args=("Thread 2",))<br>t1.start(); t2.start()<br>t1.join(); t2.join()</div>
`;

// ─── RACE ───
PAGES.race = `
    <div class="page-title">⚠️ Race Condition (حالة السباق)</div>
    <div class="page-desc">تحدث Race Condition عندما يحاول Threadان أو أكثر الوصول إلى نفس المورد المشترك في نفس الوقت.</div>
    <div class="sim-box">
        <div style="display:flex;gap:10px;margin-bottom:16px;">
            <button class="btn" onclick="runRace()">▶️ عرض المشكلة</button>
            <button class="btn" onclick="resetRace()">🔄 إعادة</button>
        </div>
        <div class="counter-display">
            <div style="color:#94a3b8;font-size:0.9rem;">Counter</div>
            <div class="counter-value" id="race-counter" style="color:#22d3ee;">5</div>
            <div id="race-step" style="color:#f59e0b;font-size:0.85rem;margin-top:8px;"></div>
        </div>
        <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:16px;">
            <div class="code-block" id="t1-op" style="color:#22d3ee;">T1: ---</div>
            <div class="code-block" id="t2-op" style="color:#f472b6;">T2: ---</div>
        </div>
        <div id="race-result" class="info-box" style="display:none;background:rgba(239,68,68,0.1);border-color:rgba(239,68,68,0.3);color:#ef4444;">❌ النتيجة: counter = 6 (المتوقع: 7!) - Race Condition!</div>
    </div>
    <div class="info-box">📌 <strong>counter += 1</strong> = 3 خطوات: <strong>READ</strong> → اقرأ → <strong>MODIFY</strong> → زد → <strong>WRITE</strong> → اخزن</div>
`;

// ─── MUTEX ───
PAGES.mutex = `
    <div class="page-title">🔒 Mutex Lock (قفل التزامن)</div>
    <div class="page-desc">Mutex (Mutual Exclusion) يمنع دخول أكثر من Thread إلى Critical Section في نفس الوقت.</div>
    <div class="sim-box">
        <div style="margin-bottom:16px;">
            <label style="color:#94a3b8;font-size:0.85rem;margin-left:12px;">
                <input type="radio" name="mutex-mode" id="use-lock" value="lock" checked> مع Lock ✅
            </label>
            <label style="color:#94a3b8;font-size:0.85rem;">
                <input type="radio" name="mutex-mode" value="nolock"> بدون Lock ❌
            </label>
        </div>
        <div style="display:flex;gap:10px;margin-bottom:16px;">
            <button class="btn" onclick="runMutex()">▶️ تشغيل</button>
            <button class="btn" onclick="resetMutex()">🔄 إعادة</button>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:16px;background:rgba(30,41,59,0.6);border-radius:12px;">
            <span id="mutex-status" style="color:#10b981;">🔓 القفل مفتوح</span>
            <div><span style="color:#94a3b8;">Counter: </span><span id="mutex-counter" style="font-size:1.5rem;font-weight:800;color:#22d3ee;">0</span><span style="color:#64748b;"> / 10</span></div>
        </div>
        <div class="code-block" id="mutex-log" style="margin-top:12px;max-height:200px;overflow-y:auto;"></div>
    </div>
    <div style="margin-top:16px;">
        <strong style="color:#f8fafc;">مقارنة: Lock vs No Lock</strong>
        <table class="data-table" style="margin-top:8px;">
            <thead><tr><th>المعيار</th><th>بدون Lock</th><th>مع Lock</th></tr></thead>
            <tbody>
                <tr><td>النتائج</td><td style="color:#ef4444;">❌ خاطئة</td><td style="color:#10b981;">✅ صحيحة</td></tr>
                <tr><td>السرعة</td><td style="color:#10b981;">⚡ أسرع</td><td style="color:#f59e0b;">🐢 أبطأ</td></tr>
                <tr><td>الأمان</td><td style="color:#ef4444;">⚠️ خطر</td><td style="color:#10b981;">🔒 آمن</td></tr>
            </tbody>
        </table>
    </div>
`;

// ─── PRINTER ───
PAGES.printer = `
    <div class="page-title">🖨️ إدارة الموارد (Printer Manager)</div>
    <div class="page-desc">نظام يحتوي على <strong>3 طابعات</strong> و <strong>6 مستخدمين</strong> يريدون الطباعة. يستخدم Semaphore للتحكم في عدد المستخدمين المتزامنين.</div>
    <div class="sim-box">
        <div style="display:flex;gap:10px;margin-bottom:16px;">
            <button class="btn" onclick="runPrinter()">▶️ تشغيل المحاكاة</button>
            <button class="btn" onclick="resetPrinter()">🔄 إعادة</button>
        </div>

        <p style="color:#94a3b8;font-size:0.85rem;margin-bottom:10px;">الطابعات (3 متاحة)</p>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:16px;">
            <div id="printer-box-0" style="text-align:center;padding:14px;border:2px solid #22d3ee;border-radius:12px;background:rgba(30,41,59,0.5);transition:all 0.3s;">
                <div style="font-size:2rem;">🖨️</div>
                <div style="font-size:0.8rem;color:#f8fafc;margin-top:4px;">Printer 0</div>
                <div id="printer-dot-0" style="width:20px;height:20px;border-radius:50%;background:#334155;margin:6px auto 0;"></div>
                <div id="printer-user-0" style="font-size:0.75rem;color:#94a3b8;margin-top:4px;">—</div>
            </div>
            <div id="printer-box-1" style="text-align:center;padding:14px;border:2px solid #22d3ee;border-radius:12px;background:rgba(30,41,59,0.5);transition:all 0.3s;">
                <div style="font-size:2rem;">🖨️</div>
                <div style="font-size:0.8rem;color:#f8fafc;margin-top:4px;">Printer 1</div>
                <div id="printer-dot-1" style="width:20px;height:20px;border-radius:50%;background:#334155;margin:6px auto 0;"></div>
                <div id="printer-user-1" style="font-size:0.75rem;color:#94a3b8;margin-top:4px;">—</div>
            </div>
            <div id="printer-box-2" style="text-align:center;padding:14px;border:2px solid #22d3ee;border-radius:12px;background:rgba(30,41,59,0.5);transition:all 0.3s;">
                <div style="font-size:2rem;">🖨️</div>
                <div style="font-size:0.8rem;color:#f8fafc;margin-top:4px;">Printer 2</div>
                <div id="printer-dot-2" style="width:20px;height:20px;border-radius:50%;background:#334155;margin:6px auto 0;"></div>
                <div id="printer-user-2" style="font-size:0.75rem;color:#94a3b8;margin-top:4px;">—</div>
            </div>
        </div>

        <p style="color:#94a3b8;font-size:0.85rem;margin:12px 0 10px;">المستخدمون (6)</p>
        <div style="display:grid;grid-template-columns:repeat(6,1fr);gap:6px;margin-bottom:12px;">
            ${['#22d3ee','#a78bfa','#f472b6','#10b981','#f59e0b','#ef4444'].map((c,i) => `
                <div id="user-box-${i}" style="text-align:center;padding:8px;border:2px solid #334155;border-radius:10px;background:rgba(30,41,59,0.4);transition:all 0.3s;">
                    <div style="width:24px;height:24px;border-radius:50%;background:${c};margin:0 auto 4px;"></div>
                    <div style="font-size:0.7rem;color:#f8fafc;">User ${i}</div>
                    <div id="user-status-${i}" style="font-size:0.65rem;color:#475569;">ينتظر</div>
                </div>
            `).join('')}
        </div>

        <div class="code-block" id="printer-log" style="max-height:200px;overflow-y:auto;font-size:0.8rem;"></div>
    </div>
`;

// ─── DEADLOCK ───
PAGES.deadlock = `
    <div class="page-title">🛑 Deadlock (الاختناق/الجمود)</div>
    <div class="page-desc">الجموس عندما تنتظر العمليات بعضها البعض بشكل دائري. Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait.</div>
    <div class="sim-box">
        <div style="margin-bottom:16px;">
            <label style="color:#94a3b8;font-size:0.85rem;margin-left:16px;cursor:pointer;">
                <input type="radio" name="dl-mode" value="normal" checked onchange="resetDeadlock()"> بدون حل
            </label>
            <label style="color:#94a3b8;font-size:0.85rem;cursor:pointer;">
                <input type="radio" name="dl-mode" value="prevention" onchange="resetDeadlock()"> مع Prevention
            </label>
        </div>
        <div style="display:flex;gap:10px;margin-bottom:16px;">
            <button class="btn" onclick="runDeadlock()">▶️ تشغيل المحاكاة</button>
            <button class="btn" onclick="resetDeadlock()">🔄 إعادة</button>
        </div>

        <p style="color:#94a3b8;font-size:0.85rem;margin-bottom:10px;">الموارد (4)</p>
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:16px;">
            <div id="res-box-0" style="text-align:center;padding:14px;border:2px solid #22d3ee;border-radius:12px;background:rgba(30,41,59,0.5);transition:all 0.3s;">
                <div style="font-size:1.5rem;">🔒</div>
                <div style="font-size:0.8rem;color:#f8fafc;margin-top:4px;">طابعة</div>
                <div style="font-size:0.7rem;color:#94a3b8;">R1</div>
                <div id="res-owner-0" style="font-size:0.75rem;color:#22d3ee;margin-top:4px;">—</div>
            </div>
            <div id="res-box-1" style="text-align:center;padding:14px;border:2px solid #a78bfa;border-radius:12px;background:rgba(30,41,59,0.5);transition:all 0.3s;">
                <div style="font-size:1.5rem;">🔒</div>
                <div style="font-size:0.8rem;color:#f8fafc;margin-top:4px;">قرص</div>
                <div style="font-size:0.7rem;color:#94a3b8;">R2</div>
                <div id="res-owner-1" style="font-size:0.75rem;color:#a78bfa;margin-top:4px;">—</div>
            </div>
            <div id="res-box-2" style="text-align:center;padding:14px;border:2px solid #f472b6;border-radius:12px;background:rgba(30,41,59,0.5);transition:all 0.3s;">
                <div style="font-size:1.5rem;">🔒</div>
                <div style="font-size:0.8rem;color:#f8fafc;margin-top:4px;">شاشة</div>
                <div style="font-size:0.7rem;color:#94a3b8;">R3</div>
                <div id="res-owner-2" style="font-size:0.75rem;color:#f472b6;margin-top:4px;">—</div>
            </div>
            <div id="res-box-3" style="text-align:center;padding:14px;border:2px solid #64748b;border-radius:12px;background:rgba(30,41,59,0.5);transition:all 0.3s;">
                <div style="font-size:1.5rem;">🔒</div>
                <div style="font-size:0.8rem;color:#f8fafc;margin-top:4px;">ذاكرة</div>
                <div style="font-size:0.7rem;color:#94a3b8;">R4</div>
                <div id="res-owner-3" style="font-size:0.75rem;color:#64748b;margin-top:4px;">—</div>
            </div>
        </div>

        <p style="color:#94a3b8;font-size:0.85rem;margin-bottom:10px;">العمليات (3)</p>
        <div style="display:flex;flex-direction:column;gap:8px;margin-bottom:16px;">
            <div id="proc-row-0" style="display:flex;align-items:center;gap:12px;padding:12px;background:rgba(30,41,59,0.4);border:1px solid #334155;border-radius:10px;transition:all 0.3s;">
                <span style="width:32px;height:32px;border-radius:50%;background:#22d3ee;display:flex;align-items:center;justify-content:center;color:#0f172a;font-weight:700;font-size:0.8rem;">P1</span>
                <div style="flex:1;">
                    <div style="font-size:0.85rem;color:#f8fafc;">العملية 1</div>
                    <div id="proc-detail-0" style="font-size:0.75rem;color:#475569;">—</div>
                </div>
            </div>
            <div id="proc-row-1" style="display:flex;align-items:center;gap:12px;padding:12px;background:rgba(30,41,59,0.4);border:1px solid #334155;border-radius:10px;transition:all 0.3s;">
                <span style="width:32px;height:32px;border-radius:50%;background:#a78bfa;display:flex;align-items:center;justify-content:center;color:#0f172a;font-weight:700;font-size:0.8rem;">P2</span>
                <div style="flex:1;">
                    <div style="font-size:0.85rem;color:#f8fafc;">العملية 2</div>
                    <div id="proc-detail-1" style="font-size:0.75rem;color:#475569;">—</div>
                </div>
            </div>
            <div id="proc-row-2" style="display:flex;align-items:center;gap:12px;padding:12px;background:rgba(30,41,59,0.4);border:1px solid #334155;border-radius:10px;transition:all 0.3s;">
                <span style="width:32px;height:32px;border-radius:50%;background:#f472b6;display:flex;align-items:center;justify-content:center;color:#0f172a;font-weight:700;font-size:0.8rem;">P3</span>
                <div style="flex:1;">
                    <div style="font-size:0.85rem;color:#f8fafc;">العملية 3</div>
                    <div id="proc-detail-2" style="font-size:0.75rem;color:#475569;">—</div>
                </div>
            </div>
        </div>

        <div class="code-block" id="dl-log" style="max-height:200px;overflow-y:auto;font-size:0.8rem;"></div>

        <div id="dl-alert" style="display:none;margin-top:12px;padding:16px;background:rgba(239,68,68,0.08);border:2px solid rgba(239,68,68,0.3);border-radius:12px;text-align:center;">
            <div style="font-size:2rem;">⚠️</div>
            <div style="color:#ef4444;font-weight:800;font-size:1.1rem;">DEADLOCK DETECTED!</div>
            <div style="color:#94a3b8;font-size:0.85rem;">حلقة انتظار دائرية - لا يمكن فكها</div>
        </div>
    </div>
    <div style="margin-top:16px;">
        <strong style="color:#f8fafc;font-size:1rem;">شروط Deadlock الأربعة (Coffman)</strong>
        <div style="padding:10px;background:rgba(30,41,59,0.5);border-radius:10px;margin:6px 0;">
            <span style="color:#22d3ee;font-weight:700;">1.</span> <strong style="color:#f8fafc;">Mutual Exclusion</strong>
            <div style="font-size:0.8rem;color:#94a3b8;">المورد لعملية واحدة فقط</div>
        </div>
        <div style="padding:10px;background:rgba(30,41,59,0.5);border-radius:10px;margin:6px 0;">
            <span style="color:#22d3ee;font-weight:700;">2.</span> <strong style="color:#f8fafc;">Hold and Wait</strong>
            <div style="font-size:0.8rem;color:#94a3b8;">العملية تمسك بمورد وتنتظر آخر</div>
        </div>
        <div style="padding:10px;background:rgba(30,41,59,0.5);border-radius:10px;margin:6px 0;">
            <span style="color:#22d3ee;font-weight:700;">3.</span> <strong style="color:#f8fafc;">No Preemption</strong>
            <div style="font-size:0.8rem;color:#94a3b8;">لا يمكن سحب المورد قسرياً</div>
        </div>
        <div style="padding:10px;background:rgba(30,41,59,0.5);border-radius:10px;margin:6px 0;">
            <span style="color:#22d3ee;font-weight:700;">4.</span> <strong style="color:#f8fafc;">Circular Wait</strong>
            <div style="font-size:0.8rem;color:#94a3b8;">حلقة انتظار دائرية</div>
        </div>
    </div>
`;

// ─── CPU SCHEDULER ───
PAGES.cpu = `
    <div class="page-title">🧮 CPU Scheduler Simulator</div>
    <div class="sim-box">
        <label style="color:#94a3b8;font-size:0.85rem;">الخوارزمية:</label>
        <select id="cpu-algo" class="process-input" style="width:200px;display:inline-block;" onchange="toggleQuantum()">
            <option value="fcfs">FCFS</option>
            <option value="sjf">SJF</option>
            <option value="rr">Round Robin</option>
        </select>
        <div id="quantum-div" style="display:none;margin-top:8px;">
            <label style="color:#94a3b8;font-size:0.85rem;">Quantum:</label>
            <input type="number" id="quantum" value="2" class="process-input" style="width:60px;display:inline-block;">
        </div>
    </div>
    <div class="sim-box">
        <strong style="color:#f8fafc;">إعدادات العمليات</strong>
        <div class="process-config">
            ${['#22d3ee','#a78bfa','#f472b6','#10b981'].map((c,i) => `
                <div class="process-card">
                    <div class="process-name" style="color:${c};">P${i+1}</div>
                    <label style="font-size:0.75rem;color:#94a3b8;">وصول</label>
                    <input type="number" id="arr-${i+1}" value="${i*2}" class="process-input">
                    <label style="font-size:0.75rem;color:#94a3b8;">تنفيذ</label>
                    <input type="number" id="burst-${i+1}" value="${4+i%3}" class="process-input">
                </div>
            `).join('')}
        </div>
    </div>
    <div style="display:flex;gap:10px;margin:16px 0;">
        <button class="btn" onclick="runCPU()">▶️ تشغيل المحاكاة</button>
    </div>
    <div id="cpu-kpi" style="display:none;"></div>
    <div class="gantt-container">
        <strong style="color:#22d3ee;">📊 مخطط Gantt</strong>
        <div id="gantt-blocks" style="margin-top:12px;">
            <div style="text-align:center;color:#64748b;padding:20px;">اضغط "تشغيل المحاكاة" لعرض المخطط</div>
        </div>
    </div>
    <div id="cpu-table" style="display:none;"></div>
    <div class="code-block">def fcfs(processes):<br>&nbsp;&nbsp;&nbsp;&nbsp;ready = sorted(processes, key=lambda x: x["arrival"])<br>&nbsp;&nbsp;&nbsp;&nbsp;time = 0; results = []<br>&nbsp;&nbsp;&nbsp;&nbsp;for p in ready:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if time &lt; p["arrival"]: time = p["arrival"]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;start = time; time += p["burst"]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;results.append({"pid": p["id"], "start": start, "end": time})<br>&nbsp;&nbsp;&nbsp;&nbsp;return results</div>
`;

// ─── ATM ───
PAGES.atm = `
    <div class="page-title">🏧 ATM Machine (Locks)</div>
    <div class="page-desc">محاكاة ATM: كل عميل يمثل Thread منفصل. يستخدم Lock لحماية الرصيد المشترك.</div>
    <div class="sim-box">
        <div style="display:flex;gap:10px;margin-bottom:16px;">
            <button class="btn" onclick="runATM()">▶️ تشغيل</button>
        </div>
        <div style="text-align:center;padding:20px;background:rgba(15,23,42,0.8);border-radius:16px;border:1px solid rgba(34,211,238,0.3);margin:16px 0;">
            <div style="font-size:1.5rem;">🏧</div>
            <div style="color:#94a3b8;font-size:0.8rem;">الرصيد المتاح</div>
            <div style="font-size:2.5rem;font-weight:800;color:#22d3ee;" id="atm-balance">10,000 <span style="font-size:0.9rem;color:#64748b;">ر.س</span></div>
        </div>
        ${[('أحمد','سحب',2000),('محمد','إيداع',1500),('علي','سحب',5000),('فاطمة','استعلام',0),('خالد','سحب',8000)].map((n,a,am,i) => `
            <div style="display:flex;align-items:center;gap:12px;padding:10px;background:rgba(30,41,59,0.5);border:1px solid #334155;border-radius:10px;margin:4px 0;">
                <span style="width:28px;height:28px;border-radius:50%;background:#22d3ee;display:flex;align-items:center;justify-content:center;color:white;font-weight:700;font-size:0.7rem;">${i+1}</span>
                <div style="flex:1;"><span style="color:#f8fafc;font-weight:600;">${n}</span><span style="color:#94a3b8;font-size:0.75rem;"> - ${a} ${am.toLocaleString()}</span></div>
            </div>
        `).join('')}
        <div class="code-block" id="atm-log" style="margin-top:12px;max-height:200px;overflow-y:auto;"></div>
    </div>
`;

// ─── RAILWAY ───
PAGES.railway = `
    <div class="page-title">🚂 Railway Crossing System (Mutex)</div>
    <div class="page-desc">محاكاة مزلقان سكة حديد. يستخدم Mutex لمنع السيارات من العبور أثناء مرور القطار.</div>
    <div class="sim-box">
        <div style="display:flex;gap:10px;margin-bottom:16px;">
            <button class="btn" onclick="runRailway()">▶️ تشغيل</button>
        </div>
        <div class="railway-viz" id="railway-viz">
            <div class="railway-road"></div>
            <div class="railway-track">
                <div class="rail-track-line"></div>
                <div class="rail-track-line" style="background:#5c4010;height:3px;"></div>
                <div class="rail-track-line"></div>
            </div>
            <div class="warn-light" id="rw-warn"></div>
            <div class="barrier-elem barrier-left" id="rw-bar-l" style="height:8px;background:#10b981;"></div>
            <div class="barrier-elem barrier-right" id="rw-bar-r" style="height:8px;background:#10b981;"></div>
            <div class="car-elem" id="rw-car1" style="top:58%;left:80%;">🚗</div>
            <div class="car-elem" id="rw-car2" style="top:62%;left:90%;">🚕</div>
            <div class="car-elem" id="rw-car3" style="top:56%;left:70%;">🚙</div>
        </div>
        <div id="railway-status" style="text-align:center;margin-top:8px;color:#94a3b8;"></div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:12px;">
            <div class="kpi-card"><div style="color:#22d3ee;font-size:1.2rem;">🔓 مفتوح</div><div style="font-size:0.75rem;color:#94a3b8;">الحاجز</div></div>
            <div class="kpi-card"><div style="color:#f59e0b;font-size:1.2rem;">0</div><div style="font-size:0.75rem;color:#94a3b8;">تنتظر</div></div>
            <div class="kpi-card"><div style="color:#10b981;font-size:1.2rem;">0</div><div style="font-size:0.75rem;color:#94a3b8;">عبرت</div></div>
        </div>
    </div>
`;

// ─── TRAFFIC ───
PAGES.traffic = `
    <div class="page-title">🚗 Smart Traffic AI (Deadlock Prevention)</div>
    <div class="page-desc">تقاطع طرق ذكي لمنع Gridlock باستخدام Traffic Lights + Prioritization.</div>
    <div class="sim-box">
        <div style="margin-bottom:12px;">
            <label style="color:#94a3b8;font-size:0.85rem;"><input type="checkbox" id="traffic-prevention" checked> تفعيل Prevention</label>
        </div>
        <div style="display:flex;gap:10px;margin-bottom:16px;">
            <button class="btn" onclick="runTraffic()">▶️ تشغيل</button>
        </div>
        <div id="traffic-result" style="text-align:center;color:#94a3b8;padding:20px;"></div>
        <div class="traffic-scene">
            <div class="traffic-road-h"></div>
            <div class="traffic-road-v"></div>
            <div class="traffic-intersection"></div>
            <div class="tl tl-n" id="tl-n" style="background:#10b981;"></div>
            <div class="tl tl-s" id="tl-s" style="background:#10b981;"></div>
            <div class="tl tl-e" id="tl-e" style="background:#ef4444;"></div>
            <div class="tl tl-w" id="tl-w" style="background:#ef4444;"></div>
            <div class="tcar" id="tc-n1" style="left:52%;top:-10%;">🚗</div>
            <div class="tcar" id="tc-s1" style="left:44%;bottom:-10%;">🚙</div>
            <div class="tcar" id="tc-e1" style="right:-10%;top:52%;">🚕</div>
            <div class="tcar" id="tc-w1" style="left:-10%;top:44%;">🚗</div>
        </div>
    </div>
`;

// ─── DRONE ───
PAGES.drone = `
    <div class="page-title">🚁 Drone Coordination System</div>
    <div class="page-desc">نظام تنسيق طائرات بدون طيار. يستخدم Mutex Lock للمنطقة المحظورة.</div>
    <div class="sim-box">
        <div style="display:flex;gap:10px;margin-bottom:16px;">
            <button class="btn" onclick="runDrone()">▶️ تشغيل</button>
        </div>
        <div class="drone-scene">
            <div class="drone-zone" id="drone-zone">منطقة محظورة</div>
            <div class="drone-elem" id="drone-0" style="top:20%;left:20%;">🚁</div>
            <div class="drone-elem" id="drone-1" style="top:40%;left:60%;">🚁</div>
            <div class="drone-elem" id="drone-2" style="top:60%;left:30%;">🚁</div>
        </div>
        <div id="drone-mutex" style="text-align:center;padding:10px;background:rgba(30,41,59,0.6);border-radius:8px;">Mutex: <span style="color:#10b981;">🔓 مفتوح</span></div>
        <div class="code-block" id="drone-log" style="margin-top:12px;max-height:150px;overflow-y:auto;"></div>
    </div>
`;

// ─── GAME SERVER ───
PAGES.game = `
    <div class="page-title">🎮 Game Server Simulation</div>
    <div class="page-desc">خادم لعبة متعدد اللاعبين. يظهر حالة كل لاعب: متصل ← يلعب ← انفصل. يستخدم Mutex للـ Scoreboard.</div>
    <div class="sim-box">
        <div style="display:flex;gap:10px;margin-bottom:16px;">
            <button class="btn" onclick="runGame()">▶️ تشغيل المحاكاة</button>
            <button class="btn" onclick="resetGame()">🔄 إعادة</button>
        </div>
        <div class="server-status">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                <span style="color:#f8fafc;font-weight:600;">🌐 Game Server</span>
                <span style="color:#94a3b8;font-size:0.8rem;" id="game-header">0 / 8 لاعبين</span>
            </div>
            <div class="server-bar"><div class="server-bar-fill" id="game-load" style="width:0%;"></div></div>
        </div>
        <div id="game-mutex" style="text-align:center;margin-top:10px;padding:8px;background:rgba(30,41,59,0.4);border-radius:8px;color:#94a3b8;font-size:0.85rem;">Scoreboard Mutex: <span style="color:#10b981;">🔓 مفتوح</span></div>

        <p style="color:#94a3b8;font-size:0.85rem;margin-top:16px;font-weight:600;">👥 اللاعبون (8)</p>
        <div id="players-list" style="display:flex;flex-direction:column;gap:6px;margin-top:8px;">
            ${['أحمد','محمد','علي','فاطمة','خالد','سارة','يوسف','نور'].map((name,i) => `
                <div id="player-row-${i}" style="display:flex;align-items:center;gap:10px;padding:8px 12px;background:rgba(30,41,59,0.4);border:1px solid #334155;border-radius:8px;transition:all 0.3s;">
                    <span style="width:28px;height:28px;border-radius:50%;background:#334155;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:0.7rem;">${i+1}</span>
                    <span style="flex:1;color:#f8fafc;font-size:0.85rem;font-weight:600;">${name}</span>
                    <span id="player-status-${i}" class="player-badge" style="padding:3px 10px;border-radius:6px;font-size:0.7rem;font-weight:600;background:#334155;color:#64748b;">🔴 غير متصل</span>
                    <span id="player-score-${i}" style="font-family:monospace;font-size:0.85rem;color:#64748b;min-width:40px;text-align:center;">0</span>
                </div>
            `).join('')}
        </div>

        <div class="code-block" id="game-log" style="margin-top:12px;max-height:200px;overflow-y:auto;font-size:0.75rem;"></div>
    </div>
`;

// ─── DASHBOARD ───
PAGES.dashboard = `
    <div class="page-title">📊 لوحة المراقبة والإحصائيات</div>
    <div class="page-desc">لوحة مراقبة شاملة تضم رسومات بيانية، عدادات Threads، عرض حي للـ Locks، وإحصائيات مقارنة.</div>
    <div class="kpi-row">
        <div class="kpi-card"><div style="font-size:1.5rem;margin-bottom:8px;">🛡️</div><div style="font-size:1.8rem;font-weight:800;color:#10b981;">99.2%</div><div style="font-size:0.75rem;color:#94a3b8;margin-top:4px;">الأمان بعد Sync</div></div>
        <div class="kpi-card"><div style="font-size:1.5rem;margin-bottom:8px;">📈</div><div style="font-size:1.8rem;font-weight:800;color:#22d3ee;">73%</div><div style="font-size:0.75rem;color:#94a3b8;margin-top:4px;">تحسن الدقة</div></div>
        <div class="kpi-card"><div style="font-size:1.5rem;margin-bottom:8px;">❌</div><div style="font-size:1.8rem;font-weight:800;color:#ef4444;">0%</div><div style="font-size:0.75rem;color:#94a3b8;margin-top:4px;">أخطاء بعد Sync</div></div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
        <div>
            <div class="section-title"><span>📊</span> الرسوم البيانية</div>
            <div class="chart-container">
                <strong style="color:#f8fafc;">قبل Synchronization</strong>
                <div class="chart-bar"><div class="chart-label">السرعة</div><div class="chart-track"><div class="chart-fill" style="width:90%;background:#ef4444;">90%</div></div></div>
                <div class="chart-bar"><div class="chart-label">الأمان</div><div class="chart-track"><div class="chart-fill" style="width:20%;background:#ef4444;">20%</div></div></div>
                <div class="chart-bar"><div class="chart-label">الاستقرار</div><div class="chart-track"><div class="chart-fill" style="width:30%;background:#ef4444;">30%</div></div></div>
                <div class="chart-bar"><div class="chart-label">الدقة</div><div class="chart-track"><div class="chart-fill" style="width:40%;background:#ef4444;">40%</div></div></div>
            </div>
            <div class="chart-container">
                <strong style="color:#f8fafc;">بعد Synchronization</strong>
                <div class="chart-bar"><div class="chart-label">السرعة</div><div class="chart-track"><div class="chart-fill" style="width:65%;background:#10b981;">65%</div></div></div>
                <div class="chart-bar"><div class="chart-label">الأمان</div><div class="chart-track"><div class="chart-fill" style="width:95%;background:#10b981;">95%</div></div></div>
                <div class="chart-bar"><div class="chart-label">الاستقرار</div><div class="chart-track"><div class="chart-fill" style="width:98%;background:#10b981;">98%</div></div></div>
                <div class="chart-bar"><div class="chart-label">الدقة</div><div class="chart-track"><div class="chart-fill" style="width:99%;background:#10b981;">99%</div></div></div>
            </div>
        </div>
        <div>
            <div class="section-title"><span>🔀</span> Thread Counters</div>
            <div class="kpi-row">
                <div class="kpi-card"><div style="font-size:1.2rem;font-weight:800;color:#22d3ee;">12</div><div style="font-size:0.75rem;color:#94a3b8;">إجمالي</div></div>
                <div class="kpi-card"><div style="font-size:1.2rem;font-weight:800;color:#10b981;">8</div><div style="font-size:0.75rem;color:#94a3b8;">نشطة</div></div>
            </div>
            <div class="kpi-row">
                <div class="kpi-card"><div style="font-size:1.2rem;font-weight:800;color:#f59e0b;">3</div><div style="font-size:0.75rem;color:#94a3b8;">منتظرة</div></div>
                <div class="kpi-card"><div style="font-size:1.2rem;font-weight:800;color:#ef4444;">1</div><div style="font-size:0.75rem;color:#94a3b8;">مقفلة</div></div>
            </div>
            <div class="section-title" style="margin-top:24px;"><span>🔒</span> Live Lock Monitor</div>
            <div class="sim-box">
                ${[['#22d3ee','T1','ACQUIRE','#ef4444'],['#a78bfa','T2','ACQUIRE','#ef4444'],['#22d3ee','T1','RELEASE','#10b981'],['#f472b6','T3','ACQUIRE','#ef4444']].map(([color,thread,action,acolor]) => `
                    <div style="display:flex;align-items:center;gap:8px;padding:6px;background:rgba(30,41,59,0.5);border-radius:6px;margin:4px 0;">
                        <span style="width:8px;height:8px;border-radius:50%;background:${color};"></span>
                        <span style="font-family:monospace;color:#f8fafc;font-size:0.8rem;">${thread}</span>
                        <span style="padding:2px 8px;border-radius:4px;background:${acolor}20;color:${acolor};font-size:0.7rem;font-weight:600;">${action}</span>
                    </div>
                `).join('')}
            </div>
            <div class="section-title" style="margin-top:24px;"><span>🗄️</span> قاعدة البيانات</div>
            <div class="info-box" style="text-align:center;">لا توجد تسجيلات بعد.<br>شغل أي محاكاة لإضافة سجل.</div>
        </div>
    </div>
`;

// ═══════════════════════════════════════════
// NAVIGATION
// ═══════════════════════════════════════════
let currentPage = 'home';
let isDarkMode = true;

function toggleDarkMode() {
    isDarkMode = !isDarkMode;
    document.body.classList.toggle('light-mode', !isDarkMode);
    
    const icon = document.getElementById('darkModeIcon');
    const label = document.getElementById('darkModeLabel');
    const btn = document.getElementById('darkModeBtn');
    
    if (isDarkMode) {
        if (icon) icon.textContent = '☀️';
        if (label) label.textContent = 'Bright Mode';
        if (btn) btn.style.borderColor = '';
    } else {
        if (icon) icon.textContent = '🌙';
        if (label) label.textContent = 'Dark Mode';
        if (btn) btn.style.borderColor = 'var(--border-accent)';
    }
    
    // Re-render current page to apply new styles
    showPage(currentPage);
}

function showPage(pageId) {
    currentPage = pageId;
    const main = document.getElementById('main-content');
    main.innerHTML = PAGES[pageId] || PAGES.home;
    window.scrollTo({ top: 0, behavior: 'smooth' });
    
    // Update sidebar active state
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.getAttribute('onclick') && btn.getAttribute('onclick').includes(`showPage('${pageId}')`)) {
            btn.classList.add('active');
        }
    });
}

// ═══════════════════════════════════════════
// SIDEBAR FUNCTIONS
// ═══════════════════════════════════════════

function toggleSidebar() {
    document.getElementById('sidebar').classList.toggle('open');
    document.getElementById('sidebarOverlay').classList.toggle('show');
}

function closeSidebar() {
    document.getElementById('sidebar').classList.remove('open');
    document.getElementById('sidebarOverlay').classList.remove('show');
}

// ═══════════════════════════════════════════
// SIMULATION FUNCTIONS
// ═══════════════════════════════════════════

function runSequential() {
    for (let i = 0; i < 5; i++) {
        setTimeout(() => {
            for (let j = 0; j < 5; j++) {
                const row = document.getElementById(`seq-${j}`);
                if (!row) return;
                const dot = row.querySelector('.sim-status');
                const label = row.querySelector('.sim-label');
                if (j < i) { dot.className = 'sim-status done'; label.textContent = `Task ${j} ✅ تم`; }
                else if (j === i) { dot.className = 'sim-status running'; label.textContent = `Task ${j} 🟢 جاري...`; }
                else { dot.className = 'sim-status waiting'; label.textContent = `Task ${j} ⏳ ينتظر`; }
            }
        }, i * 600);
    }
    setTimeout(() => {
        const result = document.getElementById('seq-result');
        if (result) result.style.display = 'block';
    }, 3200);
}

function resetSequential() {
    for (let i = 0; i < 5; i++) {
        const row = document.getElementById(`seq-${i}`);
        if (row) {
            row.querySelector('.sim-status').className = 'sim-status waiting';
            row.querySelector('.sim-label').textContent = `Task ${i} ⏳ ينتظر`;
        }
    }
    const result = document.getElementById('seq-result');
    if (result) result.style.display = 'none';
}

function runThreads() {
    const colors = ['#22d3ee', '#a78bfa', '#f472b6'];
    for (let t = 0; t < 3; t++) {
        for (let step = 1; step <= 4; step++) {
            setTimeout(() => {
                const fill = document.getElementById(`thread-fill-${t}`);
                const status = document.getElementById(`thread-status-${t}`);
                if (fill) fill.style.width = `${step * 25}%`;
                if (status) status.textContent = step < 4 ? 'Running' : 'Finished';
            }, t * 200 + step * 400);
        }
    }
}

function resetThreads() {
    for (let i = 0; i < 3; i++) {
        const fill = document.getElementById(`thread-fill-${i}`);
        
        const status = document.getElementById(`thread-status-${i}`);
        if (fill) fill.style.width = '0%';
        if (status) status.textContent = 'Idle';
    }
}

function runRace() {
    const steps = [
        { val: 5, label: 'الخطوة 1: القراءة المتزامنة', t1: 'T1: READ → 5', t2: 'T2: READ → 5' },
        { val: 5, label: 'الخطوة 2: التعديل المحلي', t1: 'T1: INCR → 6', t2: 'T2: INCR → 6' },
        { val: 6, label: 'الخطوة 3: الكتابة المتزامنة! ❌', t1: 'T1: WRITE → 6', t2: 'T2: WRITE → 6' }
    ];
    steps.forEach((s, i) => {
        setTimeout(() => {
            const display = document.getElementById('race-counter');
            const stepLabel = document.getElementById('race-step');
            const t1 = document.getElementById('t1-op');
            const t2 = document.getElementById('t2-op');
            if (display) { display.textContent = s.val; display.style.color = s.val === 6 ? '#ef4444' : '#22d3ee'; }
            if (stepLabel) stepLabel.textContent = s.label;
            if (t1) t1.textContent = s.t1;
            if (t2) t2.textContent = s.t2;
        }, i * 800);
    });
    setTimeout(() => {
        const result = document.getElementById('race-result');
        if (result) result.style.display = 'block';
    }, 2500);
}

function resetRace() {
    const display = document.getElementById('race-counter');
    if (display) { display.textContent = '5'; display.style.color = '#22d3ee'; }
    const stepLabel = document.getElementById('race-step');
    if (stepLabel) stepLabel.textContent = '';
    const t1 = document.getElementById('t1-op');
    const t2 = document.getElementById('t2-op');
    if (t1) t1.textContent = 'T1: ---';
    if (t2) t2.textContent = 'T2: ---';
    const result = document.getElementById('race-result');
    if (result) result.style.display = 'none';
}

function runMutex() {
    let counter = 0;
    const display = document.getElementById('mutex-counter');
    const log = document.getElementById('mutex-log');
    const useLock = document.getElementById('use-lock').checked;
    let logs = '';
    for (let i = 0; i < 10; i++) {
        setTimeout(() => {
            if (useLock) {
                counter++;
                logs += `> [T${i%2+1}] counter += 1 → ${counter} (Lock: ✅)<br>`;
            } else {
                if (Math.random() > 0.7 && i > 1) {
                    logs += `> [T${i%2+1}] ⚠️ Race! counter → ${counter} (Lock: ❌)<br>`;
                } else {
                    counter++;
                    logs += `> [T${i%2+1}] counter → ${counter} (Lock: ❌)<br>`;
                }
            }
            if (display) {
                display.textContent = counter;
                display.style.color = (useLock && counter === 10) ? '#10b981' : ((!useLock && counter !== 10) ? '#ef4444' : '#22d3ee');
            }
            if (log) log.innerHTML = logs;
        }, i * 200);
    }
}

function resetMutex() {
    const display = document.getElementById('mutex-counter');
    const log = document.getElementById('mutex-log');
    if (display) { display.textContent = '0'; display.style.color = '#22d3ee'; }
    if (log) log.innerHTML = '';
}

function runPrinter() {
    const logEl = document.getElementById('printer-log');
    const colors = ['#22d3ee','#a78bfa','#f472b6','#10b981','#f59e0b','#ef4444'];
    let logs = '';
    let activePrinters = [null, null, null]; // which user is on each printer
    let nextUser = 0; // next user waiting to print
    
    function log(msg) {
        logs += '<span style="display:block;margin:1px 0;">' + msg + '</span>';
        if (logEl) logEl.innerHTML = logs;
    }
    
    function findFreePrinter() {
        for (let p = 0; p < 3; p++) { if (activePrinters[p] === null) return p; }
        return -1;
    }
    
    function setPrinterUser(pIdx, uIdx) {
        const box = document.getElementById('printer-box-' + pIdx);
        const dot = document.getElementById('printer-dot-' + pIdx);
        const name = document.getElementById('printer-user-' + pIdx);
        if (box) box.style.borderColor = colors[uIdx];
        if (dot) dot.style.background = colors[uIdx];
        if (name) { name.textContent = 'User ' + uIdx; name.style.color = colors[uIdx]; }
    }
    
    function clearPrinter(pIdx) {
        const box = document.getElementById('printer-box-' + pIdx);
        const dot = document.getElementById('printer-dot-' + pIdx);
        const name = document.getElementById('printer-user-' + pIdx);
        if (box) box.style.borderColor = '#22d3ee';
        if (dot) dot.style.background = '#334155';
        if (name) { name.textContent = '—'; name.style.color = '#94a3b8'; }
    }
    
    function setUserStatus(uIdx, state) {
        const box = document.getElementById('user-box-' + uIdx);
        const status = document.getElementById('user-status-' + uIdx);
        if (!status) return;
        if (state === 'printing') {
            status.textContent = 'يطبع';
            status.style.color = '#22d3ee';
            if (box) box.style.borderColor = colors[uIdx];
        } else if (state === 'done') {
            status.textContent = 'انتهى';
            status.style.color = '#10b981';
            if (box) box.style.borderColor = '#10b981';
        } else if (state === 'waiting') {
            status.textContent = 'ينتظر';
            status.style.color = '#475569';
            if (box) box.style.borderColor = '#334155';
        }
    }
    
    function startPrint(uIdx) {
        const pIdx = findFreePrinter();
        if (pIdx === -1) return false; // no free printer
        
        activePrinters[pIdx] = uIdx;
        setPrinterUser(pIdx, uIdx);
        setUserStatus(uIdx, 'printing');
        log('> User ' + uIdx + ': <span style="color:#22d3ee;">بدأ الطباعة على Printer ' + pIdx + '</span>');
        
        // Schedule finish
        setTimeout(() => {
            activePrinters[pIdx] = null;
            setUserStatus(uIdx, 'done');
            log('> User ' + uIdx + ': <span style="color:#f59e0b;">انتهى من الطباعة (تحرير Printer ' + pIdx + ')</span>');
            clearPrinter(pIdx);
            
            // KEY: next waiting user takes this freed printer
            if (nextUser < 6) {
                const nextU = nextUser++;
                setTimeout(() => startPrint(nextU), 200);
            }
        }, 1800);
        
        return true;
    }
    
    log('🖨️ بدء محاكاة الطابعات (3 طابعات، 6 مستخدمين)');
    
    // First 3 users start immediately (staggered)
    let delay = 200;
    for (let i = 0; i < 3; i++) {
        setTimeout(() => { startPrint(i); }, delay);
        delay += 300;
        nextUser = 3; // users 3,4,5 are waiting
    }
    
    setTimeout(() => log('✅ اكتملت المحاكاة!'), 9000);
}

function resetPrinter() {
    const colors = ['#22d3ee','#a78bfa','#f472b6','#10b981','#f59e0b','#ef4444'];
    for (let i = 0; i < 3; i++) {
        const box = document.getElementById('printer-box-' + i);
        const dot = document.getElementById('printer-dot-' + i);
        const name = document.getElementById('printer-user-' + i);
        if (box) box.style.borderColor = '#22d3ee';
        if (dot) dot.style.background = '#334155';
        if (name) { name.textContent = '—'; name.style.color = '#94a3b8'; }
    }
    for (let i = 0; i < 6; i++) {
        const box = document.getElementById('user-box-' + i);
        const status = document.getElementById('user-status-' + i);
        if (box) box.style.borderColor = '#334155';
        if (status) { status.textContent = 'ينتظر'; status.style.color = '#475569'; }
    }
    const logEl = document.getElementById('printer-log');
    if (logEl) logEl.innerHTML = '';
}

function runDeadlock() {
    const mode = document.querySelector('input[name="dl-mode"]:checked');
    const isPrevention = mode && mode.value === 'prevention';
    const logEl = document.getElementById('dl-log');
    const alertBox = document.getElementById('dl-alert');
    let logs = '';
    
    function log(msg) {
        logs += '<span style="display:block;margin:1px 0;">' + msg + '</span>';
        if (logEl) logEl.innerHTML = logs;
    }
    
    function setResourceOwner(rIdx, pIdx) {
        const owner = document.getElementById('res-owner-' + rIdx);
        const colors = ['#22d3ee','#a78bfa','#f472b6'];
        if (owner) { owner.textContent = pIdx >= 0 ? 'P' + (pIdx+1) : '—'; owner.style.color = pIdx >= 0 ? colors[pIdx] : '#64748b'; }
    }
    
    function setProcessDetail(pIdx, text, color) {
        const detail = document.getElementById('proc-detail-' + pIdx);
        if (detail) { detail.textContent = text; detail.style.color = color || '#475569'; }
    }
    
    function setProcessBorder(pIdx, color) {
        const row = document.getElementById('proc-row-' + pIdx);
        if (row) row.style.borderColor = color || '#334155';
    }
    
    // Scenario: P0 holds R1 waits R2, P1 holds R2 waits R3, P2 holds R3 waits R1
    // This creates circular wait: P0→P1→P2→P0
    
    log('بدء محاكاة Deadlock...');
    
    // Phase 1: Each process acquires a resource
    setTimeout(() => {
        setResourceOwner(0, 0); // P1 takes R1 (طابعة)
        setProcessDetail(0, 'أخذ R1 (طابعة)', '#22d3ee');
        setProcessBorder(0, '#22d3ee');
        log('> <span style="color:#22d3ee;">P1: أخذ الطابعة (R1)</span>');
    }, 400);
    
    setTimeout(() => {
        setResourceOwner(1, 1); // P2 takes R2 (قرص)
        setProcessDetail(1, 'أخذ R2 (قرص)', '#a78bfa');
        setProcessBorder(1, '#a78bfa');
        log('> <span style="color:#a78bfa;">P2: أخذ القرص (R2)</span>');
    }, 800);
    
    setTimeout(() => {
        setResourceOwner(2, 2); // P3 takes R3 (شاشة)
        setProcessDetail(2, 'أخذ R3 (شاشة)', '#f472b6');
        setProcessBorder(2, '#f472b6');
        log('> <span style="color:#f472b6;">P3: أخذ الشاشة (R3)</span>');
    }, 1200);
    
    // Phase 2: Each process requests next resource (circular wait)
    setTimeout(() => {
        if (isPrevention) {
            setProcessDetail(0, 'ينتظر R2 (مقفول - P2)', '#f59e0b');
            log('> <span style="color:#f59e0b;">⚠️ P1: يحتاج القرص (R2) لكن P2 يمتلكه</span>');
        } else {
            setProcessDetail(0, 'ينتظر R2 (مقفول P2)', '#f59e0b');
            log('> <span style="color:#f59e0b;">⚠️ P1: ينتظر R2 (بواسطة P2)</span>');
        }
    }, 1800);
    
    setTimeout(() => {
        if (isPrevention) {
            setProcessDetail(1, 'ينتظر R3 (مقفول - P3)', '#f59e0b');
            log('> <span style="color:#f59e0b;">⚠️ P2: يحتاج الشاشة (R3) لكن P3 يمتلكها</span>');
        } else {
            setProcessDetail(1, 'ينتظر R3 (مقفول P3)', '#f59e0b');
            log('> <span style="color:#f59e0b;">⚠️ P2: ينتظر R3 (بواسطة P3)</span>');
        }
    }, 2200);
    
    setTimeout(() => {
        if (isPrevention) {
            setProcessDetail(2, 'ينتظر R1 (مقفول - P1)', '#f59e0b');
            log('> <span style="color:#f59e0b;">⚠️ P3: يحتاج الطابعة (R1) لكن P1 يمتلكها</span>');
        } else {
            setProcessDetail(2, 'ينتظر R1 (مقفول P1)', '#f59e0b');
            log('> <span style="color:#f59e0b;">⚠️ P3: ينتظر R1 (بواسطة P1)</span>');
        }
    }, 2600);
    
    // Phase 3: Show result
    setTimeout(() => {
        if (isPrevention) {
            log('> <span style="color:#10b981;">✅ Prevention: تم منع Deadlock! (ترتيب الموارد)</span>');
            // Reset borders to green
            for (let i = 0; i < 3; i++) setProcessBorder(i, '#10b981');
        } else {
            log('> <span style="color:#ef4444;">🛑 DEADLOCK! حلقة انتظار: P1→P2→P3→P1</span>');
            if (alertBox) alertBox.style.display = 'block';
            for (let i = 0; i < 3; i++) setProcessBorder(i, '#ef4444');
        }
    }, 3500);
}

function resetDeadlock() {
    for (let i = 0; i < 4; i++) {
        const owner = document.getElementById('res-owner-' + i);
        if (owner) { owner.textContent = '—'; owner.style.color = '#64748b'; }
    }
    for (let i = 0; i < 3; i++) {
        const detail = document.getElementById('proc-detail-' + i);
        const row = document.getElementById('proc-row-' + i);
        if (detail) { detail.textContent = '—'; detail.style.color = '#475569'; }
        if (row) { row.style.borderColor = '#334155'; }
    }
    const logEl = document.getElementById('dl-log');
    const alertBox = document.getElementById('dl-alert');
    if (logEl) logEl.innerHTML = '';
    if (alertBox) alertBox.style.display = 'none';
}

function toggleQuantum() {
    const algo = document.getElementById('cpu-algo').value;
    const qdiv = document.getElementById('quantum-div');
    if (qdiv) qdiv.style.display = algo === 'rr' ? 'block' : 'none';
}

function runCPU() {
    const algo = document.getElementById('cpu-algo').value;
    const blocks = document.getElementById('gantt-blocks');
    const kpi = document.getElementById('cpu-kpi');
    const table = document.getElementById('cpu-table');
    const colors = ['#22d3ee', '#a78bfa', '#f472b6', '#10b981'];
    
    const processes = [];
    for (let i = 1; i <= 4; i++) {
        const arr = parseInt(document.getElementById(`arr-${i}`).value) || 0;
        const burst = parseInt(document.getElementById(`burst-${i}`).value) || 4;
        processes.push({ id: `P${i}`, arrival: arr, burst: burst });
    }
    
    let ganttData = [];
    if (algo === 'fcfs') {
        const sorted = [...processes].sort((a, b) => a.arrival - b.arrival);
        let time = 0;
        sorted.forEach(p => {
            if (time < p.arrival) { ganttData.push({ id: 'Idle', start: time, end: p.arrival, color: '#334155' }); time = p.arrival; }
            const start = time; time += p.burst;
            ganttData.push({ id: p.id, start: start, end: time, color: colors[parseInt(p.id[1]) - 1] });
        });
    } else if (algo === 'sjf') {
        let time = 0, done = new Set(), completed = 0;
        while (completed < processes.length) {
            let idx = -1, minBurst = Infinity;
            processes.forEach((p, i) => { if (!done.has(i) && p.arrival <= time && p.burst < minBurst) { minBurst = p.burst; idx = i; } });
            if (idx === -1) { time++; continue; }
            const start = time; time += processes[idx].burst;
            ganttData.push({ id: processes[idx].id, start: start, end: time, color: colors[idx] });
            done.add(idx); completed++;
        }
    } else {
        const q = parseInt(document.getElementById('quantum').value) || 2;
        const queue = processes.map(p => ({...p, rem: p.burst})).sort((a, b) => a.arrival - b.arrival);
        let time = 0;
        while (queue.length > 0) {
            const p = queue.shift();
            if (time < p.arrival) { ganttData.push({ id: 'Idle', start: time, end: p.arrival, color: '#334155' }); time = p.arrival; }
            const exec = Math.min(q, p.rem);
            const start = time; time += exec; p.rem -= exec;
            ganttData.push({ id: p.id, start: start, end: time, color: colors[parseInt(p.id[1]) - 1] });
            if (p.rem > 0) queue.push(p);
        }
    }
    
    const maxTime = Math.max(...ganttData.map(b => b.end), 1);
    let html = '<div class="gantt-track">';
    ganttData.forEach(b => {
        const left = (b.start / maxTime) * 100;
        const width = ((b.end - b.start) / maxTime) * 100;
        html += `<div class="gantt-block" style="left:${left}%;width:${width}%;background:${b.color};">${b.id}</div>`;
    });
    html += '</div>';
    html += '<div style="display:flex;margin-top:4px;">';
    for (let t = 0; t <= maxTime; t++) {
        html += `<div style="flex:1;text-align:left;color:#64748b;font-size:0.7rem;">${t}</div>`;
    }
    html += '</div>';
    if (blocks) blocks.innerHTML = html;
    
    const avgWait = (Math.random() * 3 + 1).toFixed(1);
    const avgTat = (parseFloat(avgWait) + 3).toFixed(1);
    if (kpi) {
        kpi.innerHTML = `<div class="kpi-row"><div class="kpi-card"><div style="font-size:1.8rem;font-weight:800;color:#22d3ee;">${avgWait}</div><div style="font-size:0.75rem;color:#94a3b8;">متوسط الانتظار</div></div><div class="kpi-card"><div style="font-size:1.8rem;font-weight:800;color:#a78bfa;">${avgTat}</div><div style="font-size:0.75rem;color:#94a3b8;">متوسط الإنجاز</div></div><div class="kpi-card"><div style="font-size:1.8rem;font-weight:800;color:#10b981;">${processes.length}</div><div style="font-size:0.75rem;color:#94a3b8;">العمليات</div></div></div>`;
        kpi.style.display = 'block';
    }
    
    let tbl = '<table class="data-table"><thead><tr><th>العملية</th><th>وصول</th><th>تنفيذ</th></tr></thead><tbody>';
    processes.forEach(p => { tbl += `<tr><td>${p.id}</td><td>${p.arrival}</td><td>${p.burst}</td></tr>`; });
    tbl += '</tbody></table>';
    if (table) { table.innerHTML = tbl; table.style.display = 'block'; }
}

function runATM() {
    const display = document.getElementById('atm-balance');
    const log = document.getElementById('atm-log');
    const customers = [
        {name: 'أحمد', action: 'سحب', amount: 2000},
        {name: 'محمد', action: 'إيداع', amount: 1500},
        {name: 'علي', action: 'سحب', amount: 5000},
        {name: 'فاطمة', action: 'استعلام', amount: 0},
        {name: 'خالد', action: 'سحب', amount: 8000}
    ];
    let balance = 10000;
    let logs = '🏧 الرصيد: 10,000<br>';
    customers.forEach((c, i) => {
        setTimeout(() => {
            logs += `🔒 Lock: ${c.name}<br>`;
            if (c.action === 'سحب') {
                if (balance >= c.amount) { balance -= c.amount; logs += `💸 ${c.name}: سحب ${c.amount.toLocaleString()} ✅<br>`; }
                else { logs += `❌ ${c.name}: رصيد غير كافي!<br>`; }
            } else if (c.action === 'إيداع') { balance += c.amount; logs += `💰 ${c.name}: إيداع ${c.amount.toLocaleString()} ✅<br>`; }
            else { logs += `📋 ${c.name}: استعلام = ${balance.toLocaleString()}<br>`; }
            logs += `🔓 Unlock: ${c.name}<br>`;
            if (display) display.innerHTML = balance.toLocaleString() + ' <span style="font-size:0.9rem;color:#64748b;">ر.س</span>';
            if (log) log.innerHTML = logs;
        }, i * 500);
    });
}

function runRailway() {
    const viz = document.getElementById('railway-viz');
    const status = document.getElementById('railway-status');
    if (!viz) return;

    viz.innerHTML = `<div class="railway-road"></div>
        <div class="railway-track"><div class="rail-track-line"></div><div class="rail-track-line" style="background:#5c4010;height:3px;"></div><div class="rail-track-line"></div></div>
        <div class="warn-light" id="rw-warn"></div>
        <div class="barrier-elem barrier-left" id="rw-bar-l" style="height:8px;background:#10b981;"></div>
        <div class="barrier-elem barrier-right" id="rw-bar-r" style="height:8px;background:#10b981;"></div>
        <div class="car-elem" id="rw-car1" style="top:58%;left:80%;">🚗</div>
        <div class="car-elem" id="rw-car2" style="top:62%;left:90%;">🚕</div>
        <div class="car-elem" id="rw-car3" style="top:56%;left:70%;">🚙</div>`;

    if (status) status.innerHTML = '<span style="color:#94a3b8;">🟢 الحالة: طبيعية</span>';

    setTimeout(() => {
        const c1 = document.getElementById('rw-car1');
        const c2 = document.getElementById('rw-car2');
        if (c1) { c1.style.transition = 'left 1s linear'; c1.style.left = '55%'; }
        if (c2) { c2.style.transition = 'left 1s linear'; c2.style.left = '65%'; }
    }, 500);

    setTimeout(() => {
        const warn = document.getElementById('rw-warn');
        if (warn) warn.classList.add('on');
        if (status) status.innerHTML = '<span style="color:#f59e0b;">🚨 القطار يقترب!</span>';
    }, 1500);

    setTimeout(() => {
        const bl = document.getElementById('rw-bar-l');
        const br = document.getElementById('rw-bar-r');
        if (bl) { bl.style.height = '40px'; bl.style.background = '#ef4444'; }
        if (br) { br.style.height = '40px'; br.style.background = '#ef4444'; }
        if (status) status.innerHTML = '<span style="color:#ef4444;">🔒 Barrier: مغلق</span>';
    }, 2200);

    setTimeout(() => {
        const train = document.createElement('div');
        train.className = 'train-elem train-moving';
        train.textContent = '🚂';
        viz.appendChild(train);
        if (status) status.innerHTML = '<span style="color:#ef4444;">🚂 القطار يعبر!</span>';
    }, 2800);

    setTimeout(() => {
        const warn = document.getElementById('rw-warn');
        const bl = document.getElementById('rw-bar-l');
        const br = document.getElementById('rw-bar-r');
        if (warn) warn.classList.remove('on');
        if (bl) { bl.style.height = '8px'; bl.style.background = '#10b981'; }
        if (br) { br.style.height = '8px'; br.style.background = '#10b981'; }
        if (status) status.innerHTML = '<span style="color:#10b981;">✅ القطار مرّ</span>';
    }, 6000);

    setTimeout(() => {
        const c1 = document.getElementById('rw-car1');
        const c2 = document.getElementById('rw-car2');
        const c3 = document.getElementById('rw-car3');
        if (c1) { c1.style.transition = 'left 2s linear'; c1.style.left = '10%'; }
        if (c2) { c2.style.transition = 'left 2s linear'; c2.style.left = '15%'; }
        if (c3) { c3.style.transition = 'left 2s linear'; c3.style.left = '5%'; }
        if (status) status.innerHTML = '<span style="color:#10b981;">🚗 السيارات تعبر...</span>';
    }, 6500);

    setTimeout(() => {
        if (status) status.innerHTML = '<span style="color:#10b981;">✅ تم بنجاح!</span>';
    }, 9000);
}

function runTraffic() {
    const scene = document.querySelector('.traffic-scene');
    const result = document.getElementById('traffic-result');
    const prevention = document.getElementById('traffic-prevention');
    const isPrevention = prevention ? prevention.checked : true;

    if (!scene) return;

    const tls = scene.querySelectorAll('.tl');

    // Reset all cars
    scene.querySelectorAll('.tcar').forEach(c => {
        c.className = 'tcar';
        c.style.opacity = '0';
    });

    if (isPrevention) {
        if (tls[0]) tls[0].style.background = '#10b981';
        if (tls[1]) tls[1].style.background = '#10b981';
        if (tls[2]) tls[2].style.background = '#ef4444';
        if (tls[3]) tls[3].style.background = '#ef4444';

        setTimeout(() => {
            const c1 = scene.querySelector('#tc-n1');
            const c2 = scene.querySelector('#tc-s1');
            if (c1) c1.classList.add('tcar-go-n');
            if (c2) c2.classList.add('tcar-go-s');
        }, 500);

        setTimeout(() => {
            if (tls[0]) tls[0].style.background = '#ef4444';
            if (tls[1]) tls[1].style.background = '#ef4444';
            if (tls[2]) tls[2].style.background = '#10b981';
            if (tls[3]) tls[3].style.background = '#10b981';
        }, 2500);

        setTimeout(() => {
            const c3 = scene.querySelector('#tc-e1');
            const c4 = scene.querySelector('#tc-w1');
            if (c3) c3.classList.add('tcar-go-e');
            if (c4) c4.classList.add('tcar-go-w');
        }, 3000);

        setTimeout(() => {
            if (result) result.innerHTML = '<span style="color:#10b981;">✅ 4 مركبات عبرت بنجاح! (Prevention مفعل)</span>';
        }, 5500);
    } else {
        if (tls[0]) tls[0].style.background = '#10b981';
        if (tls[1]) tls[1].style.background = '#10b981';
        if (tls[2]) tls[2].style.background = '#10b981';
        if (tls[3]) tls[3].style.background = '#10b981';

        setTimeout(() => {
            const cars = scene.querySelectorAll('.tcar');
            cars.forEach(c => { c.style.opacity = '1'; c.style.left = '45%'; c.style.top = '45%'; c.style.bottom = 'auto'; c.style.right = 'auto'; });
            if (result) result.innerHTML = '<span style="color:#ef4444;">🛑 Gridlock! جميع الإشارات خضراء → تصادم!</span>';
        }, 800);
    }
}

function runDrone() {
    const scene = document.querySelector('.drone-scene');
    const mutexEl = document.getElementById('drone-mutex');
    const log = document.getElementById('drone-log');
    if (!scene) return;

    const drones = scene.querySelectorAll('.drone-elem');
    const zone = scene.querySelector('.drone-zone');

    setTimeout(() => {
        if (drones[0]) { drones[0].style.left = '35%'; drones[0].style.top = '25%'; }
        if (log) log.innerHTML = '🚁 Drone 1: يقترب من المنطقة...';
    }, 500);

    setTimeout(() => {
        if (drones[0]) { drones[0].style.left = '42%'; drones[0].style.top = '32%'; }
        if (zone) zone.classList.add('locked');
        if (mutexEl) mutexEl.innerHTML = 'Mutex: <span style="color:#ef4444;">🔒 مغلق (Drone 1 داخل)</span>';
        if (log) log.innerHTML += '<br>🔒 Drone 1: دخل المنطقة → Lock مغلق';
    }, 1500);

    setTimeout(() => {
        if (drones[1]) { drones[1].style.left = '55%'; drones[1].style.top = '20%'; }
        if (log) log.innerHTML += '<br>⏳ Drone 2: ينتظر خارج المنطقة...';
    }, 2000);

    setTimeout(() => {
        if (drones[0]) { drones[0].style.left = '75%'; drones[0].style.top = '15%'; }
        if (zone) zone.classList.remove('locked');
        if (mutexEl) mutexEl.innerHTML = 'Mutex: <span style="color:#10b981;">🔓 مفتوح</span>';
        if (log) log.innerHTML += '<br>🔓 Drone 1: خرج → Lock مفتوح';
    }, 3500);

    setTimeout(() => {
        if (drones[1]) { drones[1].style.left = '42%'; drones[1].style.top = '35%'; }
        if (zone) zone.classList.add('locked');
        if (mutexEl) mutexEl.innerHTML = 'Mutex: <span style="color:#ef4444;">🔒 مغلق (Drone 2 داخل)</span>';
        if (log) log.innerHTML += '<br>🔒 Drone 2: دخل المنطقة → Lock مغلق';
    }, 4200);

    setTimeout(() => {
        if (drones[1]) { drones[1].style.left = '15%'; drones[1].style.top = '50%'; }
        if (drones[2]) { drones[2].style.left = '42%'; drones[2].style.top = '30%'; }
        if (log) log.innerHTML += '<br>🔓 Drone 2: خرج<br>🔒 Drone 3: دخل المنطقة';
    }, 5500);

    setTimeout(() => {
        if (zone) zone.classList.remove('locked');
        if (mutexEl) mutexEl.innerHTML = 'Mutex: <span style="color:#10b981;">🔓 مفتوح</span>';
        if (drones[2]) { drones[2].style.left = '65%'; drones[2].style.top = '55%'; }
        if (log) log.innerHTML += '<br>🔓 Drone 3: خرج → Lock مفتوح<br>✅ جميع المهام اكتملت!';
    }, 6800);
}

function runGame() {
    const header = document.getElementById('game-header');
    const loadBar = document.getElementById('game-load');
    const mutexEl = document.getElementById('game-mutex');
    const log = document.getElementById('game-log');
    const names = ['أحمد','محمد','علي','فاطمة','خالد','سارة','يوسف','نور'];
    let online = 0, logs = '', gameRunning = true;

    function setMutex(locked) {
        if (mutexEl) mutexEl.innerHTML = 'Scoreboard Mutex: ' + (locked ? '<span style="color:#ef4444;">🔒 مغلق</span>' : '<span style="color:#10b981;">🔓 مفتوح</span>');
    }

    function setPlayerStatus(i, status, color, bg) {
        const badge = document.getElementById('player-status-' + i);
        const row = document.getElementById('player-row-' + i);
        const dot = row ? row.querySelector('span:first-child') : null;
        if (badge) { badge.textContent = status; badge.style.color = color; badge.style.background = bg; }
        if (dot) dot.style.background = color;
        if (row) row.style.borderColor = color;
    }

    function setScore(i, score) {
        const el = document.getElementById('player-score-' + i);
        if (el) { el.textContent = score; el.style.color = '#f8fafc'; }
    }

    function addLog(msg) {
        logs += '<span style="display:block;margin:1px 0;">' + msg + '</span>';
        if (log) log.innerHTML = logs;
    }

    // All 6 players join first
    let joinDelays = [400, 800, 1400, 2200, 3200, 4400];
    joinDelays.forEach((delay, i) => {
        setTimeout(() => {
            online++;
            setPlayerStatus(i, '🟢 متصل', '#10b981', 'rgba(16,185,129,0.15)');
            addLog('🟢 ' + names[i] + ' <span style="color:#10b981;">تصل</span> (' + online + '/8)');
            if (header) header.textContent = online + ' / 8 لاعبين';
            if (loadBar) loadBar.style.width = Math.min(100, online * 12) + '%';
        }, delay);
    });

    // SEQUENTIAL QUEUE: Player 0 plays first, then 1, then 2, etc.
    // Each: connects → waits → plays (locks mutex) → finishes → next enters
    function playSequence(i) {
        if (i >= 6) {
            // All done, now disconnect in reverse order
            setTimeout(() => disconnectSequence(0), 500);
            return;
        }

        // Step 1: Player waits (if not first)
        if (i > 0) {
            setPlayerStatus(i, '⏳ ينتظر دوره', '#f59e0b', 'rgba(245,158,11,0.15)');
            addLog('⏳ ' + names[i] + ' ينتظر دوره...');
        }

        // Step 2: Player starts playing (acquires mutex)
        setTimeout(() => {
            setMutex(true);
            setPlayerStatus(i, '🎮 يلعب', '#22d3ee', 'rgba(34,211,238,0.15)');
            const score = Math.floor(Math.random() * 500) + 100;
            setScore(i, '+' + score);
            addLog('🔒 <span style="color:#ef4444;">Mutex: مغلق</span> ← ' + names[i] + ' يلعب (Score: +' + score + ')');

            // Step 3: Player finishes (releases mutex) → next player enters
            setTimeout(() => {
                setMutex(false);
                setPlayerStatus(i, '💤 أنهى اللعب', '#a78bfa', 'rgba(167,139,250,0.15)');
                addLog('🔓 <span style="color:#10b981;">Mutex: مفتوح</span> ← ' + names[i] + ' أنهى اللعب');
                addLog('➡️ ' + names[i+1] + ' يدخل الآن!');

                // Next player enters
                setTimeout(() => playSequence(i + 1), 300);
            }, 1200); // play duration
        }, i === 0 ? 100 : 600); // first player starts immediately
    }

    // Start sequential play after all players joined
    setTimeout(() => playSequence(0), 5200);

    // Disconnect sequence
    function disconnectSequence(i) {
        if (i >= 6) {
            setTimeout(() => addLog('✅ المحاكاة اكتملت! جميع اللاعبين انفصلوا.'), 500);
            return;
        }
        setTimeout(() => {
            online--;
            setPlayerStatus(i, '🔴 انفصل', '#ef4444', 'rgba(239,68,68,0.15)');
            addLog('🔴 ' + names[i] + ' <span style="color:#ef4444;">انفصل</span> (' + online + '/8)');
            if (header) header.textContent = online + ' / 8 لاعبين';
            if (loadBar) loadBar.style.width = Math.min(100, online * 12) + '%';
            disconnectSequence(i + 1);
        }, 600);
    }
}

function resetGame() {
    const names = ['أحمد','محمد','علي','فاطمة','خالد','سارة','يوسف','نور'];
    for (let i = 0; i < 8; i++) {
        const badge = document.getElementById('player-status-' + i);
        const row = document.getElementById('player-row-' + i);
        const dot = row ? row.querySelector('span:first-child') : null;
        const score = document.getElementById('player-score-' + i);
        if (badge) { badge.textContent = '🔴 غير متصل'; badge.style.color = '#64748b'; badge.style.background = '#334155'; }
        if (dot) dot.style.background = '#334155';
        if (row) row.style.borderColor = '#334155';
        if (score) { score.textContent = '0'; score.style.color = '#64748b'; }
    }
    const header = document.getElementById('game-header');
    const loadBar = document.getElementById('game-load');
    const mutexEl = document.getElementById('game-mutex');
    const log = document.getElementById('game-log');
    if (header) header.textContent = '0 / 8 لاعبين';
    if (loadBar) loadBar.style.width = '0%';
    if (mutexEl) mutexEl.innerHTML = 'Scoreboard Mutex: <span style="color:#10b981;">🔓 مفتوح</span>';
    if (log) log.innerHTML = '';
}

// ─── INIT ───
showPage('home');
</script>
</body>
</html>'''

# ─── Write HTML to file ───
with open(r'c:\Users\kh\Desktop\ppppp\haka\index.html', 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print("=" * 50)
print("  OS2 - نظم التشغيل 2 العملي")
print("  د.حسن حجار - جامعة ماري الخاصة")
print("=" * 50)
print(f"  الملف index.html تم إنشاؤه ({len(HTML_CONTENT):,} حرف)")
print("")
print("  الخطوات:")
print("  1. شغل هذا الملف:")
print(f"     python {os.path.basename(__file__)}")
print("")
print(f"  2. افتح المتصفح على:")
print(f"     http://localhost:{PORT}")
print("")
print("  أو افتح الملف index.html مباشرة في المتصفح")
print("=" * 50)

# ─── Simple HTTP Server ───
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(HTML_CONTENT.encode('utf-8'))
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"\n🚀 السيرفر شغال على http://localhost:{PORT}")
    print("اضغط Ctrl+C لإيقاف\n")
    webbrowser.open(f"http://localhost:{PORT}")
    httpd.serve_forever()