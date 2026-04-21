import streamlit as st

# --- ページ設定 ---
st.set_page_config(page_title="Welfamily Relations OS Update", layout="centered", page_icon="🌿")

# --- Welfamilyブランド・カスタムCSS（モスグリーン基調） ---
st.markdown("""
    <style>
    /* 全体背景：目に優しい薄いグレーグリーン */
    .main { background-color: #f9faf9; }
    
    /* ヘッダー・テキスト色：深いモスグリーン */
    h1, h2, h3 { color: #2d3e2f; font-family: 'Helvetica Neue', Arial, 'Hiragino Kaku Gothic ProN', 'Hiragino Sans', sans-serif; }
    
    /* ボタンデザイン：Welfamilyモスグリーン */
    .stButton>button { 
        width: 100%; 
        border-radius: 8px; 
        height: 3.8em; 
        background-color: #4a5d4e; 
        color: white; 
        font-weight: bold; 
        font-size: 1.1em;
        border: none;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(74, 93, 78, 0.2);
    }
    .stButton>button:hover {
        background-color: #3d4d40;
        box-shadow: 0 6px 20px rgba(74, 93, 78, 0.3);
        transform: translateY(-2px);
    }

    /* 結果カード：モスグリーンのアクセントライン */
    .result-card { 
        padding: 30px; 
        border-radius: 12px; 
        background-color: white; 
        border-top: 8px solid #4a5d4e; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); 
        margin-bottom: 25px; 
    }

    /* タイプラベル */
    .type-label { 
        font-weight: bold; 
        color: #4a5d4e; 
        font-size: 1.2em; 
        border-bottom: 2px solid #c5a059; 
        padding-bottom: 5px;
        margin-bottom: 10px;
        display: inline-block;
    }

    /* Tryボックス：モスグリーンとアースゴールド */
    .try-box-m { padding: 15px; border-radius: 8px; margin-top: 10px; background-color: #f0f2f0; font-size: 0.95em; border-left: 5px solid #4a5d4e; border: 1px solid #e1e4e1; }
    .try-box-f { padding: 15px; border-radius: 8px; margin-top: 10px; background-color: #f9f5f0; font-size: 0.95em; border-left: 5px solid #c5a059; border: 1px solid #ede8e0; }
    
    /* スライダーのラベル調整 */
    .stSlider label { color: #2d3e2f; font-weight: 500; }
    </style>
    """, unsafe_allow_html=True)

# ロゴ風ヘッダー
st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>Welfamily</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; margin-top: 0; font-size: 1.3em; font-weight: normal; color: #6b7e6c;'>Relations OS Update</h2>", unsafe_allow_html=True)
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

# --- データベース：16パターン解説 & 男女別アドバイス ---
pattern_db = {
    ("A", "X"): {"title": "正論の要塞", "desc": "男性の解決策が女性の感情を論破しようとし、女性がさらに爆発する悪循環です。", "m_try": "結論を言う前に「それはしんどかったね」と5秒間、相手の感情をオウム返しに。内容より感情に光を当てて。", "f_try": "話し始める前に「今は解決策はいらないから、10分だけ聴いてほしい」と先に宣言して、彼のスイッチをオフに。"},
    ("A", "Y"): {"title": "合理性の壁", "desc": "男性の合理的な行動が女性の不安を直撃。理解し合えない孤独が深まります。", "m_try": "予定変更は「事実」だけでなく「君に寂しい思いをさせて申し訳ない」という一言を添えるだけで劇的に変わります。", "f_try": "寂しい時は「なぜ連絡くれないの？」と問わず「声が聞けなくて不安だった」とI（アイ）メッセージを伝えて。"},
    ("A", "Z"): {"title": "効率戦争", "desc": "お互いに正しさを競い合い、家庭が職場のような殺伐とした空間になりがちです。", "m_try": "正論が通っても「二人の仲が悪くなれば負け」だと心得て。あえて折れることが真の強さです。", "f_try": "彼のやり方が非効率でも、一度感謝を伝え、管理の手を少し緩めて。彼を「部下」にしないことが鍵です。"},
    ("A", "W"): {"title": "進化するバディ", "desc": "男性の分析力と女性の言語化能力が噛み合い、建設的に進歩できる関係です。", "m_try": "効率を求めすぎず、あえて「無駄な対話の時間」を確保して。心の余白が、長期的な安定を支えます。", "f_try": "彼の論理性は「冷たさ」ではなく、関係を整理するための武器。彼の頭脳を借りる感覚で接しましょう。"},
    ("B", "X"): {"title": "嵐と避難所", "desc": "女性の感情から男性が逃げ、追いかける女性がさらに激昂する構造です。", "m_try": "逃げる時は「30分頭を冷やして戻る」と復帰時間を宣言して。黙って去るのが最大のNGアクションです。", "f_try": "彼の沈黙を「拒絶」ではなく「脳のフリーズ」だと理解し、彼が言葉を探す時間を10分だけ待ってみて。"},
    ("B", "Y"): {"title": "孤独のサイレンス", "desc": "男性の沈黙が女性の不安を最大化させる、冷え込みの強いパターンです。", "m_try": "言葉が見つからなくても、隣に座る、手を握る。非言語の「僕はここにいるよ」という安心を届けてください。", "f_try": "問い詰めすぎると彼はさらに殻に。まずは「私はあなたの味方だよ」という安心信号を先に発信して。"},
    ("B", "Z"): {"title": "静かなる独裁", "desc": "女性が全てを決め、男性は従うだけ。男性に不満が溜まりやすい状態です。", "m_try": "「なんでもいい」は対話の放棄です。「僕はAよりBが好きかな」と小さな自己主張からリハビリを。", "f_try": "彼が意見を言った時は、自分の考えと違っても「教えてくれてありがとう」と一度肯定し、彼の自信を育てて。"},
    ("B", "W"): {"title": "ゆっくりした開花", "desc": "女性の忍耐強い対話で、男性が少しずつ本音を話し始める成長過程です。", "m_try": "自分の感情を「快・不快」の2択からで良いので、少しずつシェアを。彼女はあなたの本音を待っています。", "f_try": "彼の小さな成長を喜び、変化を急かさない。彼の沈黙を「思考中」と捉えるあなたの心の余裕が薬です。"},
    ("C", "X"): {"title": "砂漠の古城", "desc": "形は立派ですが情緒的な交流が枯渇。女性は心の渇きを訴えています。", "m_try": "高価なプレゼントより、毎日「今日一番嬉しかったことは？」と聞く1分間の興味を彼女に捧げてください。", "f_try": "彼の仕事への献身を「当たり前」と思わず、彼なりの不器用な愛情表現だと一度肯定してから要望を。"},
    ("C", "Y"): {"title": "遠い城", "desc": "男性は外で戦っていますが、女性は不在の孤独で壊れそうになっています。", "m_try": "離れていても「繋がっている」感覚を。風景写真1枚でいいので、日常の断片を彼女にシェアして。", "f_try": "彼の働く姿にリスペクトを。その上で「5分だけ電話したい」と控えめに、かつ具体的に要求を伝えて。"},
    ("C", "Z"): {"title": "共同経営者", "desc": "運営は完璧ですが、夫婦としての甘い空気がなくなっている状態です。", "m_try": "効率を度外視して、彼女を一人の女性として扱うデートを月1回。家庭の話をしない時間をプロデュース。"},
    ("C", "W"): {"title": "不揺の基盤", "desc": "男性の安定感と女性の成熟が合致。地に足のついた強い家族になれます。", "m_try": "安定に甘んじず、「最近の君の心の状態はどう？」と定期的なアップデートを。慣れを警戒してください。"},
    ("D", "X"): {"title": "共鳴の輪", "desc": "男性が女性の感情を包み込み、家庭内が明るいエネルギーで満たされます。", "m_try": "彼女の感情に同調しすぎて疲弊しないよう、意識的に自分の趣味や一人の時間も確保してください。"},
    ("D", "Y"): {"title": "安息の地", "desc": "男性の包容力が女性の不安を溶かす、最強の安心パターンです。", "m_try": "ハグや言葉での愛情表現をルーチンに。あなたが提供する安心が、彼女の人生の輝きを支えます。"},
    ("D", "Z"): {"title": "賢者の鏡", "desc": "お互いを高め合えます。時に真面目すぎて遊びがなくなる点に注意です。", "m_try": "彼女の完璧主義を和らげるため、あえて「テキトーでいいよ」と笑いを誘う「緩さ」を提供して。"},
    ("D", "W"): {"title": "黄金の調和", "desc": "互いを理解し、常に最新のOSにアップデートし続けるWelfamilyの到達点です。", "m_try": "今の幸せを維持するために、定期的に二人で「これから作りたい未来」をワクワク語り合いましょう。"}
}

# 16パターンの後半（D-X以降）のアドバイスが漏れないように補完
pattern_db[("C", "Z")]["f_try"] = "役割を脱ぎ捨てて甘える。隙を見せることが、彼の「守りたい」という男性本能を刺激します。"
pattern_db[("C", "W")]["f_try"] = "彼の安定感を称賛し、彼が安心して「弱音」を吐ける世界で唯一の場所になりましょう。"
pattern_db[("D", "X")]["f_try"] = "彼の優しさを当然と思わず、「話を聴いてくれて本当に救われる」と言葉でフィードバックを。"
pattern_db[("D", "Y")]["f_try"] = "貰うばかりではなく、彼が疲れている時は「私があなたのセキュリティになるね」と支えて。"
pattern_db[("D", "Z")]["f_try"] = "彼のコーチングを「コントロール」と思わず、対等な知恵として楽しんで。たまには一緒にダラダラを。"
pattern_db[("D", "W")]["f_try"] = "最高のパートナーである彼に感謝を。その余裕を、周囲の悩める方々への光としてお裾分けして。"

# --- フォーム入力 ---
st.info("💡 1:全く当てはまらない 〜 5:非常に当てはまる の5段階で回答ください")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🧔 男性セクション")
    m = [st.slider(f"Q{i+1}: {txt}", 1, 5, 3) for i, txt in enumerate([
        "悩みにはすぐアドバイスをしたくなる", "気まずくなると逃げたくなる", "形での責任（稼ぎ等）が一番大事だと思う", "事実関係の正しさを重視する", "相手の感情に共感するのが得意だ"
    ])]

with col2:
    st.markdown("### 👩 女性セクション")
    f = [st.slider(f"Q{i+1}: {txt}", 1, 5, 3) for i, txt in enumerate([
        "気持ちを分かってほしい", "不在や無関心に強い不安を感じる", "過去の不満を思い出しやすい", "自分ばかり犠牲だと思う", "状況を冷静に言語化できる"
    ])]

if st.button("総合分析を実行して、関係をアップデートする"):
    # --- 多次元スコアリング判定 ---
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
    
    # 結果カード
    st.markdown(f"""
    <div class="result-card">
        <h2 style='text-align:center;'>現在の関係性：【{res['title']}】</h2>
        <p style='font-size:1.1em; color:#333; text-align:center;'>{res['desc']}</p>
    </div>
    """, unsafe_allow_html=True)

    # 各自のタイプ
    c_m, c_f = st.columns(2)
    with c_m:
        st.markdown(f"<div class='type-label'>🧔 {type_info_m[m_type]['name']}</div>", unsafe_allow_html=True)
        st.write(type_info_m[m_type]['desc'])
    with c_f:
        st.markdown(f"<div class='type-label'>👩 {type_info_f[f_type]['name']}</div>", unsafe_allow_html=True)
        st.write(type_info_f[f_type]['desc'])

    st.divider()

    # アドバイス
    st.markdown("### 🚀 より良い関係にするための今週のTry")
    t_m, t_f = st.columns(2)
    with t_m:
        st.markdown(f"<div style='color:#4a5d4e; font-weight:bold;'>🧔 男性のTry</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='try-box-m'>{res['m_try']}</div>", unsafe_allow_html=True)
    with t_f:
        st.markdown(f"<div style='color:#c5a059; font-weight:bold;'>👩 女性のTry</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='try-box-f'>{res['f_try']}</div>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#999; font-size:0.8em;'>© 2026 Welfamily | すべての夫婦に、安心とアップデートを。</p>", unsafe_allow_html=True)
