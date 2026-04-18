import streamlit as st

# --- ページ設定 ---
st.set_page_config(page_title="Welfamily Relations OS Update", layout="centered", page_icon="🧡")

# --- カスタムCSS ---
st.markdown("""
    <style>
    .main { background-color: #fffaf0; }
    .stButton>button { 
        width: 100%; border-radius: 25px; height: 3.5em; 
        background-color: #ff6b6b; color: white; font-weight: bold; border: none;
    }
    .result-card { 
        padding: 25px; border-radius: 15px; background-color: white; 
        border-left: 10px solid #ff6b6b; box-shadow: 0 10px 25px rgba(0,0,0,0.05); margin-bottom: 25px; 
    }
    .type-label { font-weight: bold; color: #ff6b6b; font-size: 1.2em; }
    .try-box { padding: 15px; border-radius: 10px; margin-top: 10px; background-color: #fff5f5; }
    h1, h2, h3 { color: #4a4a4a; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("Welfamily Relations OS Update")
st.write("### 〜ふたりの絆を、最新版へ。〜")

# --- データベース ---
type_desc_m = {
    "A": {"name": "ロジカル・ソルジャー", "desc": "解決策命。感情より事実を優先し、効率的に問題を片付けたいタイプ。"},
    "B": {"name": "ピース・リトリーター", "desc": "争い回避型。心理的負荷がかかると沈黙や回避で自分を守るタイプ。"},
    "C": {"name": "ストイック・プロバイダー", "desc": "大黒柱型。形（経済・安定）で愛情を示そうとするが、情緒的会話が苦手なタイプ。"},
    "D": {"name": "ハイブリッド・コーチ", "desc": "Welfamilyのメソッドを体現する、感情理解と解決を両立できるタイプ。"}
}
type_desc_f = {
    "X": {"name": "エモーショナル・センサー", "desc": "共感重視型。感情が豊かで、パートナーに心の同調を強く求めるタイプ。"},
    "Y": {"name": "セキュリティ・シーカー", "desc": "安心渇望型。繋がりを確認することで安心を得たい、寂しがりなタイプ。"},
    "Z": {"name": "パーフェクト・マネージャー", "desc": "完璧主義型。犠牲感が強く、パートナーへの要求が厳しくなりがちなタイプ。"},
    "W": {"name": "ナラティブ・パートナー", "desc": "Welfamilyが目指す姿。感情を冷静に伝え、共に新しい物語を作れるタイプ。"}
}
pattern_db = {
    ("A", "X"): {"title": "正論の要塞", "desc": "男性の解決策が女性の感情を論破しようとし、女性がさらに爆発する悪循環です。"},
    ("A", "Y"): {"title": "合理性の壁", "desc": "男性の合理的な行動が女性の不安を直撃。理解し合えない孤独が深まります。"},
    ("A", "Z"): {"title": "効率戦争", "desc": "お互いに正しさを競い合い、家庭が職場のような殺伐とした空間になりがちです。"},
    ("A", "W"): {"title": "進化するバディ", "desc": "男性の分析力と女性の言語化能力が噛み合い、建設的に進歩できる関係です。"},
    ("B", "X"): {"title": "嵐と避難所", "desc": "女性の感情から男性が逃げ、追いかける女性がさらに激昂する構造です。"},
    ("B", "Y"): {"title": "孤独のサイレンス", "desc": "男性の沈黙が女性の不安を最大化させる、冷え込みの強いパターンです。"},
    ("B", "Z"): {"title": "静かなる独裁", "desc": "女性が全てを決め、男性は従うだけ。男性に不満が溜まりやすい状態です。"},
    ("B", "W"): {"title": "ゆっくりした開花", "desc": "女性の忍耐強い対話で、男性が少しずつ本音を話し始める成長過程です。"},
    ("C", "X"): {"title": "砂漠の古城", "desc": "形は立派ですが情緒的な交流が枯渇。女性は心の渇きを訴えています。"},
    ("C", "Y"): {"title": "遠い城", "desc": "男性は外で戦っていますが、女性は不在の孤独で壊れそうになっています。"},
    ("C", "Z"): {"title": "共同経営者", "desc": "運営は完璧ですが、夫婦としての甘い空気がなくなっている状態です。"},
    ("C", "W"): {"title": "不揺の基盤", "desc": "男性の安定感と女性の成熟が合致。地に足のついた強い家族になれます。"},
    ("D", "X"): {"title": "共鳴の輪", "desc": "男性が女性の感情を包み込み、家庭内が明るいエネルギーで満たされます。"},
    ("D", "Y"): {"title": "安息の地", "desc": "男性の包容力が女性の不安を溶かす、最強の安心パターンです。"},
    ("D", "Z"): {"title": "賢者の鏡", "desc": "お互いを高め合えます。時に真面目すぎて遊びがなくなる点に注意です。"},
    ("D", "W"): {"title": "黄金の調和", "desc": "互いを理解し、常に最新のOSにアップデートし続けるWelfamilyの到達点です。"}
}
# Tryメッセージは省略（前回同様のため）

# --- UI フォーム ---
st.info("💡 1:全く当てはまらない 〜 5:非常に当てはまる の5段階で回答ください")

col_m, col_f = st.columns(2)
with col_m:
    st.markdown("### 🧔 男性セクション")
    m = [st.slider(f"Q{i+1}: {text}", 1, 5, 3) for i, text in enumerate([
        "悩みにはすぐアドバイスしたい", "気まずいと逃げたくなる", "形での責任が一番大事だ", "事実関係の正しさを重視する", "共感と受け止めが得意だ"
    ])]
with col_f:
    st.markdown("### 👩 女性セクション")
    f = [st.slider(f"Q{i+1}: {text}", 1, 5, 3) for i, text in enumerate([
        "気持ちを分かってほしい", "不在や無関心に不安を感じる", "過去の不満を思い出しやすい", "自分ばかり犠牲だと思う", "状況を冷静に言語化できる"
    ])]

if st.button("総合分析を実行して、関係をアップデートする"):
    # --- 多次元スコアリング計算 ---
    s_m = {
        "A": m[0]*2 + m[1]*-1 + m[2]*1 + m[3]*2 + m[4]*-2,
        "B": m[0]*-1 + m[1]*2 + m[3]*1 + m[4]*-1,
        "C": m[0]*1 + m[2]*2 + m[3]*1,
        "D": m[1]*-2 + m[3]*-1 + m[4]*3
    }
    s_f = {
        "X": f[0]*2 + f[1]*1 + f[2]*1 + f[4]*-1,
        "Y": f[0]*1 + f[1]*2 + f[2]*1 + f[4]*-2,
        "Z": f[1]*1 + f[2]*2 + f[3]*2 + f[4]*-1,
        "W": f[0]*1 + f[3]*-2 + f[4]*3
    }
    
    m_type = max(s_m, key=s_m.get)
    f_type = max(s_f, key=s_f.get)
    
    res = pattern_db[(m_type, f_type)]
    st.balloons()
    st.markdown(f'<div class="result-card"><h2 style="text-align:center;">結果：【{res["title"]}】</h2><p>{res["desc"]}</p></div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"<span class='type-label'>🧔 {type_desc_m[m_type]['name']}</span>", unsafe_allow_html=True)
        st.write(type_desc_m[m_type]['desc'])
    with c2:
        st.markdown(f"<span class='type-label'>👩 {type_desc_f[f_type]['name']}</span>", unsafe_allow_html=True)
        st.write(type_desc_f[f_type]['desc'])
