#coding: UTF-8
import discord
import random
import ssl
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()


pile = ["攻撃1 落とし物	"+"\n"+"	念運空	"+"\n"+"	任意のプレイヤーに運命干渉を行う。"+"\n"+"\n",
"攻撃1 占術	"+"\n"+"	運空精	"+"\n"+"	相手にダメージを与えたら、あなたの手札のカード1枚で精神感応を試みてもよい。"+"\n"+"\n",
"攻撃1 野犬	"+"\n"+"	念運精	"+"\n"+"	任意のプレイヤーに運命干渉を行う。"+"\n"+"\n",
"攻撃1 滑る地面	"+"\n"+"	熱念運	"+"\n"+"	防御されなければ、次のあなたのターンまで、あなたはダメージを受けない。"+"\n"+"\n",
"攻撃1 支配	"+"\n"+"	運精	"+"\n"+"	山札の一番上のカードで精神感応を試みる。"+"\n"+"\n",
"攻撃1 揺さぶり	"+"\n"+"	念空精	"+"\n"+"	相手にダメージを与えたら、あなたの手札のカード1枚で精神感応を試みてもよい。"+"\n"+"\n",
"攻撃1 磁場	"+"\n"+"	電念運	"+"\n"+"	防御されなければ、次のあなたのターンまで、あなたはダメージを受けない。"+"\n"+"\n",
"攻撃2 漏電	"+"\n"+"	電空	"+"\n"+"	ターゲット以外のプレイヤー1人に2ダメージを与えてもよい。"+"\n"+"\n",
"攻撃2 不幸な事故	"+"\n"+"	電熱運"+"\n"+"\n",
"攻撃2 高速弾	"+"\n"+"	電熱念"+"\n"+"\n",
"攻撃2 縮地	"+"\n"+"	念空	"+"\n"+"	防御不可"+"\n"+"\n",
"攻撃2 落石	"+"\n"+"	念運	"+"\n"+"	防御不可。任意のプレイヤーに運命干渉を行う。"+"\n"+"\n",
"攻撃2 熱感	"+"\n"+"	熱精	"+"\n"+"	相手にダメージを与えたら、あなたの手札のカード1枚で精神感応を試みてもよい。"+"\n"+"\n",
"攻撃2 拷問	"+"\n"+"	念精	"+"\n"+"	相手にダメージを与えたら、あなたの手札のカード1枚で精神感応を試みてもよい。"+"\n"+"\n",
"攻撃2 運命変転	"+"\n"+"	運	"+"\n"+"	自分の縦向きの捨て札を1枚選ぶ。そのカードのダメージと効果をこのカードに追加する。"+"\n"+"\n",
"攻撃3 電磁砲	"+"\n"+"	電念	"+"\n"+"	自分に1ダメージ。防御されなければ、次のあなたのターンまで、あなたはダメージを受けない。"+"\n"+"\n",
"攻撃3 雹塊	"+"\n"+"	熱運"+"\n"+"\n",
"攻撃3 爆発	"+"\n"+"	熱念"+"\n"+"\n",
"攻撃3 落雷	"+"\n"+"	電運	"+"\n"+"	自分に1ダメージ。任意のプレイヤーに運命干渉を行う。"+"\n"+"\n",
"攻撃4 夢幻暴走	"+"\n"+"	念	"+"\n"+"	次のあなたのターンまで、あなたはダメージを受けず、レゾナンスリングを使用されない。"+"\n"+"\n",
"攻撃4 電熱ブレード	"+"\n"+"	電熱	"+"\n"+"	自分に2ダメージ。"+"\n"+"\n",
"攻撃5 完全焼却	"+"\n"+"	熱"+"\n"+"\n",
"攻撃6 衝天轟雷	"+"\n"+"	電	"+"\n"+"	自分に3ダメージ。"+"\n"+"\n",
"防御 蜃気楼	"+"\n"+"	熱空精	"+"\n"+"	防御した攻撃のダメージを2軽減する。"+"\n"+"\n",
"防御 静電気	"+"\n"+"	電空精	"+"\n"+"	防御した攻撃のダメージを2軽減する。"+"\n"+"\n",
"防御 突風	"+"\n"+"	熱空	"+"\n"+"	防御した攻撃のダメージを2軽減し、ターゲットに1ダメージを与える。"+"\n"+"\n",
"防御 高速移動	"+"\n"+"	電熱空	"+"\n"+"	防御した攻撃のダメージを1軽減し、ターゲットに1ダメージを与える。"+"\n"+"\n",
"防御 閃光	"+"\n"+"	電熱精	"+"\n"+"	防御した攻撃のダメージを1軽減し、ターゲットに1ダメージを与える。"+"\n"+"\n",
"防御 ニューロン暴走	"+"\n"+"	電精	"+"\n"+"	ターゲットに2ダメージを与える。"+"\n"+"\n",
"防御 空間識変調	"+"\n"+"	空精	"+"\n"+"	防御した攻撃のダメージを1軽減する。その後、あなたの手札のカード1枚で精神感応を試みてもよい。"+"\n"+"\n",
"防御 落とし穴	"+"\n"+"	運空	"+"\n"+"	防御した攻撃のダメージを2軽減し、任意のプレイヤーに運命干渉を行う。"+"\n"+"\n",
"防御 空間連結	"+"\n"+"	空	"+"\n"+"	防御した攻撃を無効化する。そのカードを自分の能力を無視して直ちにあなたが使用する。その後、そのカードを元々の使用者の捨て札に縦向きで置く。"+"\n"+"\n",
"防御 精神破壊	"+"\n"+"	精	"+"\n"+"	自分に4ダメージ。防御した攻撃を無効化する。あなた以外のプレイヤー全員は能力1つを使用不能にする。（能力カードを1枚選び、表にする）"+"\n"+"\n"]
attack = []
defense = []
bottrash = []
myhand = []
abilityA = ["電", "熱", "念", "運", "空", "精"]
abilityB = ["電", "熱", "念", "運", "空", "精"]

rolelist = []
rolephase = 0



startshadow = 0


list1d6 = [1, 2, 3, 4, 5, 6]
list1d4 = [1, 2, 3, 4]


list = ["刀","扇", "薙", "銃", "忍", "傘", "書", "毒", "絡", "騎", "古", "琵", "炎", "笛", "戦", "社","経", "絆","機", "新","爪","拒", "鎌", "塵", "旗","橇","鏡","櫂","兜", "槌","嵐", "棹", "面", "勾", "金", "恐"]
list2 = ["大気の護符","水の護符","火の護符","土の護符","イシュターの天秤","春の杖","時のブーツ","イオの財布","聖杯","信心深きサイラス","強欲のフィグリム","女預言者ナリア","驚愕の箱","物乞いの角笛","悪意のダイス","破壊者ケアン","首長のアムサグ","魔法の秘本","ラグフィールドの兜","運命の手","灰顔のルイス","イオリスのルーン方体","力の薬","夢の薬","知識の薬","命の薬","時の砂時計","壮大の錫杖","オラフの祝福の像","ヤンの忘れられた花瓶","精霊のアミュレット","光の木","アルカノ蛭","水晶球","暴食の大鍋","吸血の王冠","竜の頭蓋骨","アルゴスの悪魔","深き眼差しのタイタス","大気の精霊","泥棒フェアリー","アルスの呪われた書","使い魔の偶像","壊死のクリス","クシディットのランプ","ウルムの封印された箱","季節の鏡","ラグノールのペンダント","夜影のシド","オニスの忌まわしき魂", "大気の護符","水の護符","火の護符","水の護符","イシュターの天秤","春の杖","時のブーツ","イオの財布","聖杯","信心深きサイラス","強欲のフィグリム","女預言者ナリア","驚愕の箱","物乞いの角笛","悪意のダイス","破壊者ケアン","首長のアムサグ","魔法の秘本","ラグフィールドの兜","運命の手","灰顔のルイス","イオリスのルーン方体","力の薬","夢の薬","知識の薬","命の薬","時の砂時計","壮大の錫杖","オラフの祝福の像","ヤンの忘れられた花瓶","精霊のアミュレット","光の木","アルカノ蛭","水晶球","暴食の大鍋","吸血の王冠","竜の頭蓋骨","アルゴスの悪魔","深き眼差しのタイタス","大気の精霊","泥棒フェアリー","アルスの呪われた書","使い魔の偶像","壊死のクリス","クシディットのランプ","ウルムの封印された箱","季節の鏡","ラグノールのペンダント","夜影のシド","オニスの忌まわしき魂"]
list0 = ["大気の護符","水の護符","火の護符","土の護符","イシュターの天秤","春の杖","時のブーツ","イオの財布","聖杯","信心深きサイラス","強欲のフィグリム","女預言者ナリア","驚愕の箱","物乞いの角笛","悪意のダイス","破壊者ケアン","首長のアムサグ","魔法の秘本","ラグフィールドの兜","運命の手","灰顔のルイス","イオリスのルーン方体","力の薬","夢の薬","知識の薬","命の薬","時の砂時計","壮大の錫杖","オラフの祝福の像","ヤンの忘れられた花瓶","精霊のアミュレット","光の木","アルカノ蛭","水晶球","暴食の大鍋","吸血の王冠","竜の頭蓋骨","アルゴスの悪魔","深き眼差しのタイタス","大気の精霊","泥棒フェアリー","アルスの呪われた書","使い魔の偶像","壊死のクリス","クシディットのランプ","ウルムの封印された箱","季節の鏡","ラグノールのペンダント","夜影のシド","オニスの忌まわしき魂", "大気の護符","水の護符","火の護符","水の護符","イシュターの天秤","春の杖","時のブーツ","イオの財布","聖杯","信心深きサイラス","強欲のフィグリム","女預言者ナリア","驚愕の箱","物乞いの角笛","悪意のダイス","破壊者ケアン","首長のアムサグ","魔法の秘本","ラグフィールドの兜","運命の手","灰顔のルイス","イオリスのルーン方体","力の薬","夢の薬","知識の薬","命の薬","時の砂時計","壮大の錫杖","オラフの祝福の像","ヤンの忘れられた花瓶","精霊のアミュレット","光の木","アルカノ蛭","水晶球","暴食の大鍋","吸血の王冠","竜の頭蓋骨","アルゴスの悪魔","深き眼差しのタイタス","大気の精霊","泥棒フェアリー","アルスの呪われた書","使い魔の偶像","壊死のクリス","クシディットのランプ","ウルムの封印された箱","季節の鏡","ラグノールのペンダント","夜影のシド","オニスの忌まわしき魂", "アルゴスの心臓",
"豊穣の角笛",
"妖精の石碑",
"セレニアの古写本",
"イシュターの巻物",
"メソディーのランタン",
"イオリスの像",
"使い魔捕え",
"イオの変転器",
"再生の玉座",
"復活の薬",
"古代の宝石",
"ジラの盾",
"信念のダイス",
"時のアミュレット",
"不思議な望遠鏡",
"アルゴスの鷹",
"強奪者のカラス",
"アルゴスの監視者",
"ハシリドコロのネズミ",
"竜の魂",
"溶岩の核",
"運命の悪戯",
"古代の薬",
"エシールの泉",
"コロフの目盛盤",
"永遠の杯",
"冬の杖",
"墓場の護符",
"イオリスの複製装置",
"エストリアの竪琴",
"時の指輪",
"アルスのミミック",
"ヒトクイカズラ",
"ウルムの魂の牢獄",
"ラグフィールドの従者",
"アルゴスの絡みつく雑草",
"イオの手先",
"神託者オトゥス",
"狡猾なハシリドコロ",
"消し去るものイグラマル",
"逃走するスピードウォール",
"ラグフィールドのオーブ",
"水晶のタイタン"]
listdraw = ["吸血の王冠", "精霊のアミュレット", "水晶球"]
listN = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listyear = [1, 2, 3]
listmonth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
listdice6 = [1, 2, 3, 4, 5, 6]

listhato=["	a-基本	2	寄付		"	,
"	a-基本	2	願いの泉		"	,
"	a-基本	2	斥候		"	,
"	a-基本	2	早馬		"	,
"	a-基本	3	交易船		"	,
"	a-基本	3	御用商人		"	,
"	a-基本	3	召集令状		"	,
"	a-基本	3	焼き畑農業		"	,
"	a-基本	4	図書館		"	,
"	a-基本	4	追い立てられた魔獣		"	,
"	a-基本	4	都市開発		"	,
"	a-基本	4	金貸し		"	,
"	a-基本	4	補給部隊		"	,
"	a-基本	5	冒険者		"	,
"	a-基本	5	呪詛の魔女		"	,
"	a-基本	5	銀行		"	,
"	a-基本	5	皇室領		"	,
"	a-基本	5	錬金術師		"	,
"	a-基本	6	噂好きの公爵夫人		"	,
"	b-極東	2	お金好きの妖精		"	,
"	b-極東	3	課税		"	,
"	b-極東	3	貿易商人		"	,
"	b-極東	3	伝書鳩		"	,
"	b-極東	4	見習い魔女		"	,
"	b-極東	4	鉱山都市		"	,
"	b-極東	4	港町		"	,
"	b-極東	5	結盟		"	,
"	c-北限	2	ケットシー		"	,
"	c-北限	2	幸運の銀貨		"	,
"	c-北限	3	洗礼		"	,
"	c-北限	3	名馬		"	,
"	c-北限	3	呪いの人形		"	,
"	c-北限	4	ドワーフの宝石職人		"	,
"	c-北限	4	宮廷闘争		"	,
"	c-北限	4	エルフの狙撃手		"	,
"	c-北限	5	地方役人		"	,
"	c-北限	5	豪商		"	,
"	c-北限	5	貴族の一人娘		"	,
"	c-北限	6	独占		"	,
"	c-北限	6	工業都市		"	,
"	d-FG	2	家守の精霊		"	,
"	d-FG	2	春風の妖精		"	,
"	d-FG	2	伝令		"	,
"	d-FG	2	密偵		"	,
"	d-FG	2	巡礼		"	,
"	d-FG	3	リーフフェアリー		"	,
"	d-FG	3	司書		"	,
"	d-FG	3	旅芸人		"	,
"	d-FG	3	祝福		"	,
"	d-FG	3	ギルドマスター		"	,
"	d-FG	3	星巫女の託宣		"	,
"	d-FG	4	ブラウニー		"	,
"	d-FG	4	氷雪の精霊		"	,
"	d-FG	4	石弓隊		"	,
"	d-FG	4	行商人		"	,
"	d-FG	4	辻占い師		"	,
"	d-FG	4	ニンフ		"	,
"	d-FG	4	大農園		"	,
"	d-FG	4	御料地		"	,
"	d-FG	4	検地役人		"	,
"	d-FG	5	商船団		"	,
"	d-FG	5	執事		"	,
"	d-FG	5	徴税人		"	,
"	d-FG	5	聖堂騎士		"	,
"	d-FG	5	鬼族の戦士		"	,
"	d-FG	5	交易都市		"	,
"	d-FG	5	収穫祭		"	,
"	d-FG	5	合併		"	,
"	d-FG	5	メイド長		"	,
"	d-FG	6	裁判官		"	,
"	e-六都	2	漁村		"	,
"	e-六都	3	いたずら妖精(不運)		"	,
"	e-六都	3	へそくり		"	,
"	e-六都	3	女学院		"	,
"	e-六都	4	まじない師(不運)		"	,
"	e-六都	4	開発命令		"	,
"	e-六都	4	魔法のランプ(不運)		"	,
"	e-六都	5	傭兵団		"	,
"	e-六都	5	免罪符		"	,
"	e-六都	5	十字軍		"	,
"	e-六都	5	砲兵部隊		"	,
"	e-六都	5	学術都市		"	,
"	e-六都	5	独立都市		"	,
"	e-六都	5	転売屋		"	,
"	e-六都	5	ニンジャマスター		"	,
"	e-六都	12	大公爵		"	,
"	f-星天	3	灯台		"	,
"	f-星天	4	先行投資		"	,
"	f-星天	4	義賊		"	,
"	f-星天	4	カンフーマスター		"	,
"	f-星天	4	家庭教師		"	,
"	f-星天	5	キョンシー		"	,
"	f-星天	5	ウイッチドクター		"	,
"	f-星天	5	キャラバン		"	,
"	f-星天	5	離れ小島		"	,
"	f-星天	5	富豪の愛娘		"
]


start = 0
Hard = 0

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 書き込み文が「megami3」で始まるか調べる
    if message.content.startswith("megami3"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            random.shuffle(list)
            m = str(list[0]+list[1]+list[2]) + "とか良いんじゃないですか？"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

    if message.content.startswith("megami2"):
        if client.user != message.author:
            random.shuffle(list)
            m = str(list[0]+list[1]) + "とか良いんじゃないですか？"
            await message.channel.send(m)

    if message.content.startswith("daima9"):
        if client.user != message.author:
            random.shuffle(list2)
            random.shuffle(listN)
            m = message.author.name + "さんの束は" + list2[0]+"・"+list2[1]+"・"+list2[2]+"・"+list2[3]+"・"+list2[4]+"・"+list2[5]+"・"+list2[6]+"・"+list2[7]+"・"+list2[8] + "ですね。左から" + str(listN[0]) + "番目をピックするのがオススメです！"
            await message.channel.send(m)
            
    if message.content.startswith("all9"):
        if client.user != message.author:
            random.shuffle(list0)
            random.shuffle(listN)
            m = message.author.name + "さんの束は" + list0[0]+"・"+list0[1]+"・"+list0[2]+"・"+list0[3]+"・"+list0[4]+"・"+list0[5]+"・"+list0[6]+"・"+list0[7]+"・"+list0[8] + "ですね。左から" + str(listN[0]) + "番目をピックするのがオススメです！"
            await message.channel.send(m)

    if message.content == "uranai":
        if client.user != message.author:
            random.shuffle(list2)
            random.shuffle(listdraw)
            m = message.author.name + "さんの今日の運勢は" + listdraw[0] + "で"+ list2[0] + "を引くくらいの運勢です。"
            await message.channel.send(m)
            
    if message.content == "uranaiall":
        if client.user != message.author:
            random.shuffle(list0)
            random.shuffle(listdraw)
            random.shuffle(listyear)
            random.shuffle(listmonth)
            m = message.author.name + "さんの今日の運勢は" + str(listyear[0]) + "年目" + str(listmonth[0]) + "月に" + listdraw[0] + "で"+ list0[0] + "を引くくらいの運勢です。"
            await message.channel.send(m)
            
    if message.content == "d":
        if client.user != message.author:
            random.shuffle(listdice6)
            m ="出目は" + str(listdice6[0]) + "です。"
            await message.channel.send(m)
            
    if message.content == "d1":
        if client.user != message.author:
            random.shuffle(list2)
            m = list2[0] + "を引きました。"
            await message.channel.send(m)
            
    if message.content == "d2":
        if client.user != message.author:
            random.shuffle(list2)
            m = list2[0] +"・"+list2[1] + "を引きました。"
            await message.channel.send(m)
            
            
    if message.content == "a1":
        if client.user != message.author:
            random.shuffle(list0)
            m = list0[0] + "を引きました。"
            await message.channel.send(m)
            
    if message.content == "a2":
        if client.user != message.author:
            random.shuffle(list0)
            m = list0[0] +"・"+list0[1] + "を引きました。"
            await message.channel.send(m)
            
    if message.content == "d4":
        if client.user != message.author:
            random.shuffle(list2)
            m = list2[0] +"・"+list2[1] +"・"+list2[2] + "・"+list2[3] + "を引きました。"
            await message.channel.send(m)
            
    if message.content == "a4":
        if client.user != message.author:
            random.shuffle(list0)
            m = list0[0] +"・"+list0[1] +"・"+list0[2] + "・"+list0[3] + "を引きました。"
            await message.channel.send(m)

    if message.content.startswith("hato"):
        if client.user != message.author:
            random.shuffle(listhato)
            newlisthato = [listhato[0], listhato[1], listhato[2],listhato[3], listhato[4], listhato[5],listhato[6], listhato[7], listhato[8], listhato[9] ]
            newlisthato.sort()
            m = "__ランダム10種__"+"\n"+"\n"+str(newlisthato[0])+"\n"+str(newlisthato[1])+"\n"+str(newlisthato[2])+"\n"+str(newlisthato[3])+"\n"+str(newlisthato[4])+"\n"+str(newlisthato[5])+"\n"+str(newlisthato[6])+"\n"+str(newlisthato[7])+"\n"+str(newlisthato[8])+"\n"+str(newlisthato[9])
            await message.channel.send(m)

    if message.content.startswith("ping"):
        if client.user != message.author:
            m = "pong"
            await message.channel.send(m)

    if message.content.startswith("name"):
        if client.user != message.author:
            m = "torisan"
            await message.channel.send(m)
            
    if message.content == "cube":
        if client.user != message.author:
            result = [random.randint(1, 6) for i in range(78)]
            await message.channel.send(str(result.count(1))+"枚、"+str(result.count(2))+"枚、"+str(result.count(3))+"枚、"+str(result.count(4))+"枚、"+str(result.count(5))+"枚、"+str(result.count(6))+"枚")

            
   
    global start, pile, attack, defense, bottrash, myhand, abilityA, abilityB, ability1, ability2, ability3, bothand, player, botactive, Hard
    if message.content == "hard":
        Hard = 1
        await message.channel.send("【Hard mode】に変更しました。"+"\n"+"レゾナンスリング成功条件: 能力3つ当て")

    if message.content == "normal":
        Hard = 0
        await message.channel.send("【normal mode】に変更しました。"+"\n"+"レゾナンスリング成功条件: 能力3つ中2つ当て")
    
    
    if message.content=="サイレントファントム" and start ==0:
        start = 1
        #bot側能力決定
        botability = random.sample(abilityA, k = 3)
        player = random.sample(abilityB, k = 3)
        ability1 = botability[0]
        ability2 = botability[1]
        ability3 = botability[2]

        #bot初期札1枚目
        m1 = ''.join(random.sample(pile, k=1))
        pile.remove(m1)

        if m1.startswith("攻撃"):
            attack.append(m1)


        if m1.startswith("防御"):
            defense.append(m1)
        
        #bot初期札2枚目
        m2 = ''.join(random.sample(pile, k=1))
        pile.remove(m2)

        if m2.startswith("攻撃"):
            attack.append(m2)

        if m2.startswith("防御"):
            defense.append(m2)

        bothand = attack+defense
        
        #プレイヤー側初期札2枚
        m3 = ''.join(random.sample(pile, k=1))
        pile.remove(m3)
        myhand.append(m3)

        m4 = ''.join(random.sample(pile, k=1))
        pile.remove(m4)
        myhand.append(m4)

        m = "サイレントファントムを開始しました。各コマンドは『help』と入力すれば見れます。"+"\n"+"\n"+"あなたの能力は"+"**"+player[0]+player[1]+player[2]+"**"+"です。"+"\n"+"\n"+"あなたの手札は"+"\n"+"\n"+m3+m4+"です。"
        await message.channel.send(m)

    #bot側ターンを"you"コマンドで開始
    if (message.content == "you" and start == 1) or (message.content == "you" and start == 2) or (message.content == "you" and start == 6) or (message.content == "you" and start == 8) or (message.content == "you" and start == 15) or (message.content == "you" and start == 16):
        m = ''.join(random.sample(pile, k=1))
        pile.remove(m)

        if m.startswith("攻撃"):
            attack.append(m)

        if m.startswith("防御"):
            defense.append(m)
        
        bothand = attack+defense
        start = 3

    if start == 3:
        botactivehand = [s for s in attack if (ability1 in s) or (ability2 in s) or (ability3 in s)]

        if len(botactivehand) >= 1 and start == 3:
            me = botactivehand[0]
            attack.remove(me)
            bottrash.append(me)
            start = 4
            bothand = attack+defense
            await message.channel.send(me+"を使います。")

        elif len(botactivehand) == 0 and start == 3:
            start = 4
            bothand = attack+defense
            await message.channel.send("カードを使わずターン終了します。")

    if message.content == "yourhand" and start == 4:
        m = ''.join(bothand)
        await message.channel.send(m)

    if (message.content == "myhand" and start == 4) or (message.content == "myhand" and start == 9):
        m = ''.join(myhand)
        await message.channel.send(m)


    if message.content.startswith("防御") and start == 4:
        if client.user != message.author:
            bothand = attack+defense
            start = 9
            for name in myhand:
                if message.content in name:
                    myhand.remove(name)
                    await message.channel.send("防御札を確認しました。")
                    break

    if message.content == "yourunmei" and start == 9:
        if len(bothand) >=1:
            ma = bothand[0]

            for x in attack:
                if ma in x:
                    attack.remove(x)
                    break

            for x in defense:
                if ma in x:
                    defense.remove(x)
                    break

            m = ''.join(random.sample(pile, k=1))
            pile.remove(m)
            start = 11
            await message.channel.send("あなたは"+ma+"を見て山札底に置きました。"+"\n"+"私はカードを1枚引きました。")

            if m.startswith("攻撃") and start ==11:
                start = 12
                attack.append(m)

            elif m.startswith("防御") and start ==11:
                start = 12
                defense.append(m)

            bothand = attack+defense


        if len(bothand) == 0 and start ==9:
            start = 12
            await message.channel.send("私はカードを持っていないので、運命干渉は起こりませんでした。") 



    if (message.content == "myturn" and start == 4) or (message.content == "myturn" and start == 9) or (message.content == "myturn" and start == 8) or (message.content == "myturn" and start == 12) or (message.content == "myturn" and start == 15) or (message.content == "myturn" and start == 16):
        start = 2
        m = ''.join(random.sample(pile, k=1))
        pile.remove(m)
        myhand.append(m)
        await message.channel.send("あなたは"+"\n"+"\n"+m+"を引きました。")

    if message.content == "yourhand" and start == 2:
        m = ''.join(bothand)
        await message.channel.send(m)

    if message.content == "myhand" and start == 2:
        m = ''.join(myhand)
        await message.channel.send(m)

    if message.content == "reso" and start == 2 and Hard == 0:
        start = 5
        await message.channel.send("レゾナンスリング宣言を確認しました。私の能力名を電熱念運空精の中から2つ書いてください。"+"\n"+"例: 熱運")
        return

    if (message.content == ability1+ability2 and start ==5) or (message.content == ability2+ability3 and start ==5) or (message.content == ability1+ability3 and start ==5) or (message.content == ability2+ability1 and start ==5) or (message.content == ability3+ability2 and start ==5) or (message.content == ability3+ability1 and start ==5):
        if client.user != message.author:
            start = 1
            await message.channel.send("レゾナンスリング成功！あなたの勝利です！"+"\n"+"能力:"+ability1+ability2+ability3)

    if message.content == "reso" and start == 2 and Hard == 1:
        start = 20
        await message.channel.send("【hard mode】"+"\n"+"レゾナンスリング宣言を確認しました。私の能力名を電熱念運空精の中から3つ書いてください。"+"\n"+"例: 電熱運")
        return

    if (message.content == ability1+ability2+ability3 and start ==20) or (message.content == ability2+ability3+ability1 and start ==20) or (message.content == ability1+ability3+ability2 and start ==20) or (message.content == ability2+ability1+ability3 and start ==20) or (message.content == ability3+ability2+ability1 and start ==20) or (message.content == ability3+ability1+ability2 and start ==20):
        if client.user != message.author:
            start = 1
            await message.channel.send("レゾナンスリング大成功！あなたの完全勝利です！"+"\n"+"能力:"+ability1+ability2+ability3)

    if message.content != ability1+ability2 and start ==5 or message.content != ability2+ability3 and start ==5 or message.content != ability1+ability3 and start ==5 or message.content != ability2+ability1 and start ==5 or message.content != ability3+ability2 and start ==5 or message.content != ability3+ability1 and start ==5:
        if client.user != message.author:
            start = 1
            await message.channel.send("レゾナンスリング失敗、5ダメージを受けてください。")

    if (message.content != ability1+ability2+ability3 and start ==20) or (message.content != ability2+ability3+ability1 and start ==20) or (message.content != ability1+ability3+ability2 and start ==20) or (message.content != ability2+ability1+ability3 and start ==20) or (message.content != ability3+ability2+ability1 and start ==20) or (message.content != ability3+ability1+ability2 and start ==20):
        if client.user != message.author:
            start = 1
            await message.channel.send("レゾナンスリング失敗、5ダメージを受けてください。")

    if message.content.startswith("攻撃") and start == 2:
        if client.user != message.author:
            botactivehand = [s for s in defense if (ability1 in s) or (ability2 in s) or (ability3 in s)]
            start = 1
            for name in myhand:
                if message.content in name:
                    myhand.remove(name)

            
                    if "防御不可" in name:
                        start = 6
                        await message.channel.send("防御不可により手札は使いません。")
                    break

            if len(botactivehand) >= 1 and start ==1:
                me = botactivehand[0]
                defense.remove(me)
                bottrash.append(me)
                bothand = attack+defense
                start = 6
                await message.channel.send(me+"を使います。")


            elif len(botactivehand) == 0 and start ==1:
                start = 6
                await message.channel.send("防御は使いません。")
                

    if message.content == "yourhand" and start == 6:
        m = ''.join(bothand)
        await message.channel.send(m)

    if message.content == "myhand" and start == 6:
        m = ''.join(myhand)
        await message.channel.send(m)

    if message.content == "yourunmei" and start == 6:
        if len(bothand) >=1:
            ma = bothand[0]

            for x in attack:
                if ma in x:
                    attack.remove(x)
                    break

            for x in defense:
                if ma in x:
                    defense.remove(x)
                    break


            m = ''.join(random.sample(pile, k=1))
            pile.remove(m)
            start = 7
            await message.channel.send("あなたは"+ma+"を見て山札底に置きました。"+"\n"+"私はカードを1枚引きました。")

            if m.startswith("攻撃") and start ==7:
                start = 8
                attack.append(m)

            elif m.startswith("防御") and start ==7:
                start = 8
                defense.append(m)

            bothand = attack+defense


        if len(bothand) == 0 and start ==6:
            start = 8
            await message.channel.send("私はカードを持っていないので、運命変転は起こりませんでした。")  

    #ランダムでmyhandからリムーブ、pileからランダムドロー、pileからリムーブ、何が抜かれて何を引いたかメッセージ
    if (message.content == "myunmei" and start == 4) or (message.content == "myunmei" and start == 9) or (message.content == "myunmei" and start ==6) or (message.content == "myunmei" and start ==12):
        g = ''.join(random.sample(myhand, k=1))
        myhand.remove(g)
        z = ''.join(random.sample(pile, k=1))
        pile.remove(z)
        myhand.append(z)
        start = 16
        await message.channel.send(g+"を確認して山札底に置きました。"+"\n"+"あなたは"+"\n"+"\n"+z+"を引きました。")



    #ハンドからなら、yourunmeiと同じ要領でattackやdefenseからリムーブし、mytrashへ。山札ならpileからランダム→pileからリムーブ→mytrashへ（botresoなしなら省略？）
    if (message.content == "yourseisin" and start == 6) or (message.content == "yourseisin" and start == 9):
        start = 15
        await message.channel.send("精神感応に使うカードを宣言してください。")

    if (message.content.startswith("攻撃") and start == 15) or (message.content.startswith("防御") and start == 15):
        start = 16
        for name in myhand:
            if message.content in name:
                myhand.remove(name)
                    

                if ability1 in name or ability2 in name or ability3 in name:
                    await message.channel.send("そのカードは使えます。")

                else:
                    await message.channel.send("そのカードは使えません。")
                    break

    if message.content.startswith("山札") and start == 15:
        y = ''.join(random.sample(pile, k=1))
        pile.remove(y)
        start = 16

        if ability1 in y or ability2 in y or ability3 in y:
            bottrash.append(y)
            await message.channel.send("山札トップのカードは"+"\n"+"\n"+y+"でした。そのカードは使えます。")

        else:
            await message.channel.send("山札トップのカードは"+"\n"+"\n"+y+"でした。そのカードは使えません。")

    #myunmeiとpile
    #if message.content == "myseisin":

    #''joinでok
    if message.content == "yourtrash":
        m = ''.join(bottrash)
        await message.channel.send(m)

    #同じだが、botresoがないなら省略？
    #if message.content == "mytrash":
    
    if message.content == "y":
        bothand = attack+defense
        m = len(bothand)
        f = ''.join(bottrash)
        await message.channel.send("手札:"+str(m)+"枚"+"\n"+"\n"+"捨て札:"+"\n"+f)

    if message.content == "m":
        m = ''.join(player)
        f = ''.join(myhand)
        await message.channel.send("能力:"+m+"\n"+"\n"+"手札:"+"\n"+f)

    if message.content == "checkstart":
        await message.channel.send("start ="+str(start))


    if message.content == "help":
        await message.channel.send("コマンド一覧"+"\n"+"\n"+"**you**: ターンを渡す。"+"\n"+"**myturn**: ターンをもらう。"+"\n"+"**y**: 相手の状態を表示する。(手札枚数、捨て札)"+"\n"+"**m**: 自分の状態を確認する。(能力、手札)"+"\n"+"**reso**: レソナンスリング使用。"+"\n"+"**yourseisin**: 相手に対して精神感応を行う。手札の場合はカードを記入(例: 攻撃3 発火)。山札トップの場合は『山札』と記入。**yourunmei**: 相手に対して運命干渉を行う。"+"\n"+"**myunmei**: 自分に運命干渉がなされる。"+"\n"+"**hakai**: 自分が『防御 精神破壊』を使用した後に打つ。相手の能力が1つ開示される。（使用不能にはならない）"+"\n"+"**win**: 勝利宣言。HPを削り切った時に打つ。"+"\n"+"**lose**: 敗北宣言。HPが削り切られた時に打つ。"+"\n"+"**end**: ゲームを終了するときに打つ。(必須)"+"\n"+"\n"+"__攻撃・防御の処理__"+"\n"+"攻撃札・防御を使用するときは、『攻撃3 発火』や『防御 精神破壊』のように記入。（対応能力名やカード説明は記入しない）")

    if message.content == "hakai":
        await message.channel.send("精神破壊により"+ability1+"を開示しました。")

    if message.content == "botactivehand":
        botactive = [s for s in defense if (ability1 in s) or (ability2 in s) or (ability3 in s)]+[d for d in attack if (ability1 in d) or (ability2 in d)or (ability3 in d)]
        await message.channel.send(''.join(botactive))

    if message.content == "yourhand":
        bothand = attack + defense
        await message.channel.send(''.join(bothand))


    if message.content == "win":
        await message.channel.send("おめでとうございます！あなたの勝利です！"+"\n"+"能力:"+ability1+ability2+ability3)

    if message.content == "lose":
        await message.channel.send("私の勝利です！"+"\n"+"能力:"+ability1+ability2+ability3)

    if message.content == "end":
        start = 0
        pile = ["攻撃1 落とし物	"+"\n"+"	念運空	"+"\n"+"	任意のプレイヤーに運命干渉を行う。"+"\n"+"\n",
"攻撃1 占術	"+"\n"+"	運空精	"+"\n"+"	相手にダメージを与えたら、あなたの手札のカード1枚で精神感応を試みてもよい。"+"\n"+"\n",
"攻撃1 野犬	"+"\n"+"	念運精	"+"\n"+"	任意のプレイヤーに運命干渉を行う。"+"\n"+"\n",
"攻撃1 滑る地面	"+"\n"+"	熱念運	"+"\n"+"	防御されなければ、次のあなたのターンまで、あなたはダメージを受けない。"+"\n"+"\n",
"攻撃1 支配	"+"\n"+"	運精	"+"\n"+"	山札の一番上のカードで精神感応を試みる。"+"\n"+"\n",
"攻撃1 揺さぶり	"+"\n"+"	念空精	"+"\n"+"	相手にダメージを与えたら、あなたの手札のカード1枚で精神感応を試みてもよい。"+"\n"+"\n",
"攻撃1 磁場	"+"\n"+"	電念運	"+"\n"+"	防御されなければ、次のあなたのターンまで、あなたはダメージを受けない。"+"\n"+"\n",
"攻撃2 漏電	"+"\n"+"	電空	"+"\n"+"	ターゲット以外のプレイヤー1人に2ダメージを与えてもよい。"+"\n"+"\n",
"攻撃2 不幸な事故	"+"\n"+"	電熱運"+"\n"+"\n",
"攻撃2 高速弾	"+"\n"+"	電熱念"+"\n"+"\n",
"攻撃2 縮地	"+"\n"+"	念空	"+"\n"+"	防御不可"+"\n"+"\n",
"攻撃2 落石	"+"\n"+"	念運	"+"\n"+"	防御不可。任意のプレイヤーに運命干渉を行う。"+"\n"+"\n",
"攻撃2 熱感	"+"\n"+"	熱精	"+"\n"+"	相手にダメージを与えたら、あなたの手札のカード1枚で精神感応を試みてもよい。"+"\n"+"\n",
"攻撃2 拷問	"+"\n"+"	念精	"+"\n"+"	相手にダメージを与えたら、あなたの手札のカード1枚で精神感応を試みてもよい。"+"\n"+"\n",
"攻撃2 運命変転	"+"\n"+"	運	"+"\n"+"	自分の縦向きの捨て札を1枚選ぶ。そのカードのダメージと効果をこのカードに追加する。"+"\n"+"\n",
"攻撃3 電磁砲	"+"\n"+"	電念	"+"\n"+"	自分に1ダメージ。防御されなければ、次のあなたのターンまで、あなたはダメージを受けない。"+"\n"+"\n",
"攻撃3 雹塊	"+"\n"+"	熱運"+"\n"+"\n",
"攻撃3 爆発	"+"\n"+"	熱念"+"\n"+"\n",
"攻撃3 落雷	"+"\n"+"	電運	"+"\n"+"	自分に1ダメージ。任意のプレイヤーに運命干渉を行う。"+"\n"+"\n",
"攻撃4 夢幻暴走	"+"\n"+"	念	"+"\n"+"	次のあなたのターンまで、あなたはダメージを受けず、レゾナンスリングを使用されない。"+"\n"+"\n",
"攻撃4 電熱ブレード	"+"\n"+"	電熱	"+"\n"+"	自分に2ダメージ。"+"\n"+"\n",
"攻撃5 完全焼却	"+"\n"+"	熱"+"\n"+"\n",
"攻撃6 衝天轟雷	"+"\n"+"	電	"+"\n"+"	自分に3ダメージ。"+"\n"+"\n",
"防御 蜃気楼	"+"\n"+"	熱空精	"+"\n"+"	防御した攻撃のダメージを2軽減する。"+"\n"+"\n",
"防御 静電気	"+"\n"+"	電空精	"+"\n"+"	防御した攻撃のダメージを2軽減する。"+"\n"+"\n",
"防御 突風	"+"\n"+"	熱空	"+"\n"+"	防御した攻撃のダメージを2軽減し、ターゲットに1ダメージを与える。"+"\n"+"\n",
"防御 高速移動	"+"\n"+"	電熱空	"+"\n"+"	防御した攻撃のダメージを1軽減し、ターゲットに1ダメージを与える。"+"\n"+"\n",
"防御 閃光	"+"\n"+"	電熱精	"+"\n"+"	防御した攻撃のダメージを1軽減し、ターゲットに1ダメージを与える。"+"\n"+"\n",
"防御 ニューロン暴走	"+"\n"+"	電精	"+"\n"+"	ターゲットに2ダメージを与える。"+"\n"+"\n",
"防御 空間識変調	"+"\n"+"	空精	"+"\n"+"	防御した攻撃のダメージを1軽減する。その後、あなたの手札のカード1枚で精神感応を試みてもよい。"+"\n"+"\n",
"防御 落とし穴	"+"\n"+"	運空	"+"\n"+"	防御した攻撃のダメージを2軽減し、任意のプレイヤーに運命干渉を行う。"+"\n"+"\n",
"防御 空間連結	"+"\n"+"	空	"+"\n"+"	防御した攻撃を無効化する。そのカードを自分の能力を無視して直ちにあなたが使用する。その後、そのカードを元々の使用者の捨て札に縦向きで置く。"+"\n"+"\n",
"防御 精神破壊	"+"\n"+"	精	"+"\n"+"	自分に4ダメージ。防御した攻撃を無効化する。あなた以外のプレイヤー全員は能力1つを使用不能にする。（能力カードを1枚選び、表にする）"+"\n"+"\n"]
        attack = []
        defense = []
        bottrash = []
        myhand = []
        abilityA = ["電", "熱", "念", "運", "空", "精"]
        abilityB = ["電", "熱", "念", "運", "空", "精"]
        Hard = 0
        await message.channel.send("ｻｲﾚﾝﾄﾌｧﾝﾄﾑ ｼｭｳﾘｮｳ ｼﾀ｡ｵｶﾀﾂﾞｹ..(((ノ〇▲)ノ")
        






client.run(token)
