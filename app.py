import streamlit as st

# --- ページ設定 ---
st.set_page_config(page_title="Welfamily Relations OS Update", layout="centered", page_icon="🧡")

# --- Welfamilyブランド・カスタムCSS ---
st.markdown("""
    <style>
    /* 全体背景 */
    .main { background-color: #f4f7f9; }
    
    /* ヘッダー・テキスト色 */
    h1, h2, h3 { color: #1a3b5d; font-family: 'Helvetica Neue', Arial, 'Hiragino Kaku Gothic ProN', 'Hiragino Sans', sans-serif; }
    
    /* ボタンデザイン：Welfamilyオレンジ */
    .stButton>button { 
        width: 100%; 
        border-radius: 8px; 
        height: 3.8em; 
        background-color: #f08300; 
        color: white; 
        font-weight: bold; 
        font-size: 1.1em;
        border: none;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(240, 131, 0, 0.3);
    }
    .stButton>button:hover {
        background-color: #e67e22;
        box-shadow: 0 6px 20px rgba(240, 131, 0, 0.4);
        transform: translateY(-2px);
    }

    /* 結果カード：Welfamilyネイビーのアクセント */
    .result-card { 
        padding: 30px; 
        border-radius: 12px; 
        background-color: white; 
        border-top: 8px solid #1a3b5d; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); 
        margin-bottom: 25px; 
    }

    /* タイプラベル */
    .type-label { 
        font-weight: bold; 
        color: #1a3b5d; 
        font-size: 1.2em; 
        border-bottom: 2px solid #f08300;
        padding-bottom: 5px;
        margin-bottom: 10px;
        display: inline-block;
    }

    /* Tryボックス：信頼のネイビーと温かみのオレンジ */
    .try-box-m { padding: 15px; border-radius: 8px; margin-top: 10px; background-color: #eef2f6; font-size: 0.95em; border-left: 5px solid #1a3b5d; }
    .try-box-f { padding: 15px; border-radius: 8px; margin-top: 10px; background-color: #fff4e6; font-size: 0.95em; border-left: 5px solid #f08300; }
    
    /* スライダーのラベル調整 */
    .stSlider label { color: #1a3b5d; font-weight: 500; }
    </style>
    """, unsafe_allow_html=True)

# ロゴの代わりにテキストでブランド表示
st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>Welfamily</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; margin-top: 0; font-size: 1.5em; font-weight: normal;'>Relations OS Update</h2>", unsafe_allow_html=True)
st.write("---")

# --- データベース：タイプ解説 ---
type_info_m = {
    "A": {"name": "ロジカル・ソルジャー", "desc": "解決策命。感情より事実を優先し、効率的に問題を片付けたいタイプ。"},
    "B": {"name": "ピース・リトリーター", "desc": "争い回避型。心理的負荷がかかると沈黙や回避で自分を守るタイプ。"},
    "C": {"name": "ストイック・プロバイダー", "desc": "大黒柱型。形（経済・安定）で愛情を示そうとするが、情緒的会話が苦手なタイプ。"},
    "D": {"name": "ハイブリッド・コーチ", "desc": "Welfamilyのメソッドを体現する、感情理解と解決を両立できるタイプ。"}
}
type_info_f = {
    "X": {"name": "エモーショナル・センサー", "desc": "共感重視型。感情が豊かで、パートナーに心の同調を強く求めるタイプ。"},
    "Y": {"name": "セキュリティ・シーカー", "desc": "安心渇望型。繋がりを確認することで安心を得たい、寂しがりなタイプ。"},
    "Z": {"name": "パーフェクト・マネージャー", "desc": "完璧主義型。犠牲感が強く、パートナーへの要求が厳しくなりがちなタイプ。"},
    "W": {"name": "ナラティブ・パートナー", "desc": "Welfamilyが目指す姿。感情を冷静に伝え、共に新しい物語を作れるタイプ。"}
}

# --- データベース：16パターン解説 ---
pattern_db = {
    ("A", "X"): {"title": "正論の要塞", "desc": "男性の解決策が女性の感情を論破しようとし、女性がさらに爆発する悪循環です。", "m_try": "結論を言う前に「それはしんどかったね」と5秒間、相手の感情をオウム返しにしてください。", "f_try": "話し始める前に「今は解決策はいらないから、10分だけ聴いてほしい」とルールを先に伝えましょう。"},
    ("A", "Y"): {"title": "合理性の壁", "desc": "男性の合理的な行動が女性の不安を直撃。理解し合えない孤独が深まります。", "m_try": "予定変更は「事実」だけでなく「君に寂しい思いをさせて申し訳ない」という感情をセットで。", "f_try": "寂しい時は「なぜ連絡くれないの？」ではなく「声が聞けなくて不安だった」と主語を自分に。"},
    ("A", "Z"): {"title": "効率戦争", "desc": "お互いに正しさを競い合い、家庭が職場のような殺伐とした空間になりがちです。", "m_try": "正論が通っても「二人の仲が悪くなれば負け」だと心得て、あえて折れる勇気を。", "f_try": "彼のやり方が非効率でも、一度感謝を伝え、管理の手を少し緩めてみましょう。"},
    ("A", "W"): {"title": "進化するバディ", "desc": "男性の分析力と女性の言語化能力が噛み合い、建設的に進歩できる関係です。", "m_try": "効率を求めすぎず、あえて「無駄な対話の時間」を確保して心のゆとりを。", "f_try": "彼の論理性は「冷たさ」ではなく、関係を整理するための強力な武器だと捉えましょう。"},
    ("B", "X"): {"title": "嵐と避難所", "desc": "女性の感情から男性が逃げ、追いかける女性がさらに激昂する構造です。", "m_try": "逃げる時は「30分頭を冷やして戻る」と復帰時間を宣言してから席を立ってください。", "f_try": "彼の沈黙を「拒絶」ではなく「脳のフリーズ」だと理解し、言葉を探す時間を待ってあげて。"},
    ("B", "Y"): {"title": "孤独のサイレンス", "desc": "男性の沈黙が女性の不安を最大化させる、冷え込みの強いパターンです。", "m_try": "言葉が見つからなくても、隣に座る、手を握るなど「身体的な安心」を提供してください。", "f_try": "問い詰めすぎると彼はさらに逃げます。「私はあなたの味方だよ」という信号を先に出して。"},
    ("B", "Z"): {"title": "静かなる独裁", "desc": "女性が全てを決め、男性は従うだけ。男性に不満が溜まりやすい状態です。", "m_try": "「なんでもいい」を封印し、「僕はAよりBが好きかな」と小さな自己主張から始めましょう。", "f_try": "彼が意見を言った時は、自分の意見と違っても「教えてくれてありがとう」と一度受け入れて。"},
    ("B", "W"): {"title": "ゆっくりした開花", "desc": "女性の忍耐強い対話で、男性が少しずつ本音を話し始める成長過程です。", "m_try": "自分の感情を「快・不快」の2択からで良いので、少しずつ言語化してシェアしましょう。", "f_try": "彼の小さな成長を喜び、変化を急かさない。彼の沈黙を「思考中」と捉えてください。"},
    ("C", "X"): {"title": "砂漠の古城", "desc": "形は立派ですが情緒的な交流が枯渇。女性は心の渇きを訴えています。", "m_try": "高価なプレゼントより、毎日「今日一番嬉しかったことは？」と聞く1分間の興味を。", "f_try": "彼の仕事への献身を当たり前と思わず、それが彼なりの愛情表現だと一度肯定しましょう。"},
    ("C", "Y"): {"title": "遠い城", "desc": "男性は外で戦っていますが、女性は不在の孤独で壊れそうになっています。", "m_try": "離れていても「繋がっている」感覚を（写真1枚でも可）意識的に提供してください。", "f_try": "彼の働く姿にリスペクトを送りつつ、「5分だけ電話したい」と具体的に要求しましょう。"},
    ("C", "Z"): {"title": "共同経営者", "desc": "運営は完璧ですが、夫婦としての甘い空気がなくなっている状態です。", "m_try": "効率を度外視して、彼女を一人の女性として扱うデートを月に1回プロデュースを。", "f_try": "役割（母親・妻）を脱ぎ捨てて、彼に甘える時間を作る。隙を見せることが彼の意欲を刺激します。"},
    ("C", "W"): {"title": "不揺の基盤", "desc": "男性の安定感と女性の成熟が合致。地に足のついた強い家族になれます。", "m_try": "安定に甘んじず、「最近の君の心の状態はどう？」と定期的なアップデートを。", "f_try": "彼の安定感を称賛し、彼が安心して弱音を吐ける唯一の場所になりましょう。"},
    ("D", "X"): {"title": "共鳴の輪", "desc": "男性が女性の感情を包み込み、家庭内が明るいエネルギーで満たされます。", "m_try": "彼女の感情に同調しすぎて自分まで疲弊しないよう、意識的に自分の時間を確保して。", "f_try": "彼の優しさを当然と思わず、「話を聴いてくれて本当に救われる」と言葉で伝えましょう。"},
    ("D", "Y"): {"title": "安息の地", "desc": "男性の包容力が女性の不安を溶かす、最強の安心パターンです。", "m_try": "ハグや言葉での愛情表現をルーチン化して継続してください。安心感の維持が鍵です。", "f_try": "貰うばかりではなく、彼が疲れている時に「私があなたのセキュリティになるね」と支えて。"},
    ("D", "Z"): {"title": "賢者の鏡", "desc": "お互いを高め合えます。時に真面目すぎて遊びがなくなる点に注意です。", "m_try": "彼女の完璧主義を和らげるため、あえて「テキトーでいいよ」と笑いを誘う余裕を。", "f_try": "彼のコーチングを「コントロール」と思わず、対等な知恵として楽しんでください。"},
    ("D", "W"): {"title": "黄金の調和", "desc": "互いを理解し、常に最新のOSにアップデートし続けるWelfamilyの到達点です。", "m_try": "今の幸せを維持するために、定期的に二人で「これから作りたい未来」を語り合いましょう。", "f_try": "最高のパートナーである彼に感謝し、その関係性を周囲にもお裾分けしましょう。"}
}

# --- フォーム入力 ---
st.info("💡 1:全く当てはまらない 〜 5:非常に当てはまる の5段階で回答ください")

st.markdown("### 🧔 男性セクション")
m_input = [st.slider(f"{i+1}. {txt}", 1, 5, 3) for i, txt in enumerate([
    "悩みにはすぐ具体的なアドバイスをしたくなる", 
    "気まずくなると黙り込んだり逃げたくなる", 
    "稼ぐことや家を建てる等の『形』が一番の責任だと思う", 
    "話し合いでは感情より事実関係の正しさを重視する", 
    "相手の感情に共感し、まずは受け止めることが得意だ"
])]

st.divider()

st.markdown("### 👩 女性セクション")
f_input = [st.slider(f"{i+1}. {txt}", 1, 5, 3) for i, txt in enumerate([
    "解決策よりも、まずは気持ちを分かってほしい", 
    "夫の不在や無関心に強い不安（セキュリティ不足）を感じる", 
    "喧嘩をすると過去の嫌な記憶を芋づる式に思い出しやすい", 
    "自分ばかりが犠牲になって家庭を守っていると感じる", 
    "自分の感情や状況を、主観だけでなく冷静に言語化できる"
])]

if st.button("総合分析を実行して、関係をアップデートする"):
    # --- 多次元スコアリング判定 ---
    s_m = {
        "A": m_input[0]*2 + m_input[1]*-1 + m_input[2]*1 + m_input[3]*2 + m_input[4]*-2,
        "B": m_input[0]*-1 + m_input[1]*2 + m_input[2]*0 + m_input[3]*1 + m_input[4]*-1,
        "C": m_input[0]*1 + m_input[1]*0 + m_input[2]*2 + m_input[3]*1 + m_input[4]*0,
        "D": m_input[0]*0 + m_input[1]*-2 + m_input[2]*0 + m_input[3]*-1 + m_input[4]*3
    }
    s_f = {
        "X": f_input[0]*2 + f_input[1]*1 + f_input[2]*1 + f_input[3]*0 + f_input[4]*-1,
        "Y": f_input[0]*1 + f_input[1]*2 + f_input[2]*1 + f_input[3]*1 + f_input[4]*-2,
        "Z": f_input[0]*0 + f_input[1]*1 + f_input[2]*2 + f_input[3]*2 + f_input[4]*-1,
        "W": f_input[0]*1 + f_input[1]*-1 + f_input[2]*-1 + f_input[3]*-2 + f_input[4]*3
    }
    m_type = max(s_m, key=s_m.get)
    f_type = max(s_f, key=s_f.get)
    
    res = pattern_db[(m_type, f_type)]
    st.balloons()
    
    # 診断結果カード（Welfamilyネイビーをテーマに）
    st.markdown(f"""
    <div class="result-card">
        <h2 style='text-align:center;'>現在の関係性：【{res['title']}】</h2>
        <p style='font-size:1.1em; color:#333; text-align:center;'>{res['desc']}</p>
    </div>
    """, unsafe_allow_html=True)

    # 各自のタイプ
    col_tm, col_tf = st.columns(2)
    with col_tm:
        st.markdown(f"<div class='type-label'>🧔 {type_info_m[m_type]['name']}</div>", unsafe_allow_html=True)
        st.write(type_info_m[m_type]['desc'])
    with col_tf:
        st.markdown(f"<div class='type-label'>👩 {type_info_f[f_type]['name']}</div>", unsafe_allow_html=True)
        st.write(type_info_f[f_type]['desc'])

    st.divider()

    # 男女別アドバイス
    st.markdown("### 🚀 より良い関係にするための今週のTry")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"<div style='color:#1a3b5d; font-weight:bold;'>🧔 男性のTry</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='try-box-m'>{res['m_try']}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div style='color:#f08300; font-weight:bold;'>👩 女性のTry</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='try-box-f'>{res['f_try']}</div>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='text-align:center; color:#999;'>© 2026 Welfamily - パートナーシップのアップデートを支援します</p>", unsafe_allow_html=True)
