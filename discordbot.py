#coding: UTF-8
from discord.ext import commands
import os
import traceback
import discord
import random
import ssl
import emoji


token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

list= ["刀","扇", "薙", "銃", "忍", "傘", "書", "毒", "絡", "騎", "古", "琵", "炎", "笛", "戦", "社","経", "絆","機", "新","爪","拒", "鎌", "塵", "旗","橇","鏡","櫂","兜", "槌","嵐", "棹", "面", "勾", "金", "恐"]
list2 = ["大気の護符","水の護符","火の護符","土の護符","イシュターの天秤","春の杖","時のブーツ","イオの財布","聖杯","信心深きサイラス","強欲のフィグリム","女預言者ナリア","驚愕の箱","物乞いの角笛","悪意のダイス","破壊者ケアン","首長のアムサグ","魔法の秘本","ラグフィールドの兜","運命の手","灰顔のルイス","イオリスのルーン方体","力の薬","夢の薬","知識の薬","命の薬","時の砂時計","壮大の錫杖","オラフの祝福の像","ヤンの忘れられた花瓶","精霊のアミュレット","光の木","アルカノ蛭","水晶球","暴食の大鍋","吸血の王冠","竜の頭蓋骨","アルゴスの悪魔","深き眼差しのタイタス","大気の精霊","泥棒フェアリー","アルスの呪われた書","使い魔の偶像","壊死のクリス","クシディットのランプ","ウルムの封印された箱","季節の鏡","ラグノールのペンダント","夜影のシド","オニスの忌まわしき魂", "大気の護符","水の護符","火の護符","水の護符","イシュターの天秤","春の杖","時のブーツ","イオの財布","聖杯","信心深きサイラス","強欲のフィグリム","女預言者ナリア","驚愕の箱","物乞いの角笛","悪意のダイス","破壊者ケアン","首長のアムサグ","魔法の秘本","ラグフィールドの兜","運命の手","灰顔のルイス","イオリスのルーン方体","力の薬","夢の薬","知識の薬","命の薬","時の砂時計","壮大の錫杖","オラフの祝福の像","ヤンの忘れられた花瓶","精霊のアミュレット","光の木","アルカノ蛭","水晶球","暴食の大鍋","吸血の王冠","竜の頭蓋骨","アルゴスの悪魔","深き眼差しのタイタス","大気の精霊","泥棒フェアリー","アルスの呪われた書","使い魔の偶像","壊死のクリス","クシディットのランプ","ウルムの封印された箱","季節の鏡","ラグノールのペンダント","夜影のシド","オニスの忌まわしき魂"]
list3 = ["吸血の王冠", "精霊のアミュレット", "水晶球", "力の薬"]
list4=[":spades:A",":spades:2", ":spades:3",":spades:4", ":spades:5",":spades:6", ":spades:7",":spades:8", ":spades:9",":spades:10", ":spades:J",":spades:Q",":spades:K",":hearts:A", ":hearts:2", ":hearts:3", ":hearts:4", ":hearts:5", ":hearts:6",":hearts:7", ":hearts:8", ":hearts:9", ":hearts:10", ":hearts:J", ":hearts:Q", ":hearts:K", ":clubs:A", ":clubs:2", ":clubs:3", ":clubs:4", ":clubs:5", ":clubs:6",":clubs:7", ":clubs:8", ":clubs:9", ":clubs:10", ":clubs:J", ":clubs:Q", ":clubs:K",":diamonds:A",":diamonds:2", ":diamonds:3",":diamonds:4", ":diamonds:5", ":diamonds:6",":diamonds:7", ":diamonds:8", ":diamonds:9", ":diamonds:10", ":diamonds:J", ":diamonds:Q", ":diamonds:K"]
list5=[":spades:A",":spades:2", ":spades:3",":spades:4", ":spades:5",":spades:6", ":spades:7",":spades:8", ":spades:9",":spades:10", ":spades:J",":spades:Q",":spades:K",":hearts:A", ":hearts:2", ":hearts:3", ":hearts:4", ":hearts:5", ":hearts:6",":hearts:7", ":hearts:8", ":hearts:9", ":hearts:10", ":hearts:J", ":hearts:Q", ":hearts:K", ":clubs:A", ":clubs:2", ":clubs:3", ":clubs:4", ":clubs:5", ":clubs:6",":clubs:7", ":clubs:8", ":clubs:9", ":clubs:10", ":clubs:J", ":clubs:Q", ":clubs:K",":diamonds:A",":diamonds:2", ":diamonds:3",":diamonds:4", ":diamonds:5", ":diamonds:6",":diamonds:7", ":diamonds:8", ":diamonds:9", ":diamonds:10", ":diamonds:J", ":diamonds:Q", ":diamonds:K", "Jo"]
listN = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list6=["	a-基本	2	寄付		"	,
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

list7=["	ほら吹き	"	,
"	収入役	"	,
"	愛人	"	,
"	炭焼き	"	,
"	畑番	"	,
"	出来高労働者	"	,
"	柴結び	"	,
"	農場管理	"	,
"	屋根がけ	"	,
"	葦集め	"	,
"	レンガ職人	"	,
"	イチゴ集め	"	,
"	木こり	"	,
"	羊農	"	,
"	小売人	"	,
"	露天商の女	"	,
"	家畜追い	"	,
"	季節労働者	"	,
"	柵管理人	"	,
"	鋤手	"	,
"	左官屋	"	,
"	君主	"	,
"	学者	"	,
"	キノコ探し	"	,
"	ブリキ職人	"	,
"	石切り	"	,
"	乳母	"	,
"	彫刻家	"	,
"	パン職人	"	,
"	居候	"	,
"	資材商人	"	,
"	レンガ貼り	"	,
"	柵見張り	"	,
"	庭師	"	,
"	族長	"	,
"	材木買い付け人	"	,
"	大工	"	,
"	種屋	"	,
"	ネズミ捕り	"	,
"	商人	"	,
"	鋤鍛冶	"	,
"	木材運び	"	,
"	レンガ大工	"	,
"	柵運び	"	,
"	畑商人	"	,
"	レンガ混ぜ	"	,
"	工場主	"	,
"	族長の娘	"	,
"	ギルド長	"	,
"	村長	"	,
"	養父母	"	,
"	家庭教師	"	,
"	鋤職人	"	,
"	牛の飼育士	"	,
"	代官	"	,
"	行商人	"	,
"	木材配り	"	,
"	石運び	"	,
"	木材集め	"	,
"	井戸掘り	"	,
"	柵立て	"	,
"	火酒作り	"	,
"	八百屋	"	,
"	有機農業者	"	,
"	共同体長	"	,
"	レンガ運び	"	,
"	改築屋	"	,
"	革なめし工	"	,
"	大農場管理人	"	,
"	販売人	"	,
"	召使	"	,
"	レンガ積み	"	,
"	修理屋	"	,
"	畜殺人	"	,
"	村の長老	"	,
"	小作人	"	,
"	てき屋	"	,
"	自由農夫	"	,
"	網漁師	"	,
"	港湾労働者	"	,
"	ブラシ作り	"	,
"	漁師	"	,
"	建築士	"	,
"	執事	"	,
"	石工	"	,
"	陶工	"	,
"	水運び	"	,
"	石持ち	"	,
"	托鉢僧	"	,
"	木大工	"	,
"	梁打ち	"	,
"	肉屋	"	,
"	調教師	"	,
"	畑農	"	,
"	厩番	"	,
"	収穫手伝い	"	,
"	醸造師	"	,
"	旋盤職人	"	,
"	大学者	"	,
"	家具職人	"	,
"	パン屋	"	,
"	メイド	"	,
"	厩作り	"	,
"	林務官	"	,
"	小農夫	"	,
"	精肉屋	"	,
"	畑作人	"	,
]

list8=["	レンガの屋根	"	,
"	木の家増築	"	,
"	カブ畑	"	,
"	石切り場	"	,
"	酒場	"	,
"	葦の家	"	,
"	ヤギ	"	,
"	木挽き台	"	,
"	レンガの柱	"	,
"	毛皮	"	,
"	林	"	,
"	斧	"	,
"	牛車	"	,
"	簗	"	,
"	搾乳台	"	,
"	レンガ置き場	"	,
"	カヌー	"	,
"	小麦車	"	,
"	地固め機	"	,
"	ヴィラ	"	,
"	ほうき	"	,
"	柄付き網	"	,
"	穀物スコップ	"	,
"	寝室	"	,
"	はしご	"	,
"	本棚	"	,
"	個人の森	"	,
"	織機	"	,
"	白鳥の湖	"	,
"	檻	"	,
"	小牧場	"	,
"	葦の池	"	,
"	レンガ杭	"	,
"	果物の木	"	,
"	レンガの家増築	"	,
"	鋤車	"	,
"	畑	"	,
"	温室	"	,
"	投げ縄	"	,
"	木骨の小屋	"	,
"	いかだ	"	,
"	レタス畑	"	,
"	簡易かまど	"	,
"	調理場	"	,
"	プランター	"	,
"	ミツバチの巣	"	,
"	折り返し鋤	"	,
"	調理コーナー	"	,
"	突き鋤	"	,
"	森の牧場	"	,
"	石ばさみ	"	,
"	書き机	"	,
"	村の井戸	"	,
"	石の家増築	"	,
"	木の宝石箱	"	,
"	ハト小屋	"	,
"	パン焼き桶	"	,
"	石車	"	,
"	鴨の池	"	,
"	木のスリッパ	"	,
"	釣竿	"	,
"	耕運鋤	"	,
"	レンガ道	"	,
"	鉤型鋤	"	,
"	葦の交換	"	,
"	イチゴ花壇	"	,
"	ガチョウ池	"	,
"	穀物の束	"	,
"	鶏小屋	"	,
"	木材荷車	"	,
"	柴屋根	"	,
"	聖マリア像	"	,
"	林道	"	,
"	わら小屋	"	,
"	ウマ	"	,
"	家畜庭	"	,
"	穀物倉庫	"	,
"	喜捨	"	,
"	木のクレーン	"	,
"	パン焼き暖炉	"	,
"	かめ	"	,
"	くまで	"	,
"	畜殺場	"	,
"	へら	"	,
"	かいば桶	"	,
"	石の交換	"	,
"	陶器	"	,
"	建築資材	"	,
"	離れのトイレ	"	,
"	薬草畑	"	,
"	親切な隣人	"	,
"	くびき	"	,
"	建築用木材	"	,
"	パン焼き部屋	"	,
"	牧人の杖	"	,
"	パン焼き小屋	"	,
"	鯉の池	"	,
"	じゃがいも堀り	"	,
"	製材所	"	,
"	荷車	"	,
"	動物園	"	,
"	ゲスト	"	,
"	マメ畑	"	,
"	火酒製造所	"	,
"	平地	"	,
"	厩	"	,
"	木の暖炉	"	,
"	肥溜め	"	,
"	馬鋤	"	,
"	酪農場	"	,
"	猪の飼育	"	,
"	家畜市場	"	,
"	強力餌	"	,
"	風車小屋	"	,
"	舗装道路	"	,
"	スパイス	"	,
"	パン焼き棒	"	,
"	水飲み場	"	,
"	脱穀そり	"	,
"	焼き串	"	,
"	露店	"	,
"	堆肥	"	,
"	家畜の餌	"	,
"	三つ足やかん	"	,
"	醸造所	"	,
"	脱穀棒	"	,
"	かご	"	,
"	乾燥小屋	"	,
"	手挽き臼	"	,
"	かんな	"	,
"	雑木林	"	,
"	がらがら	"	,
"	角笛	"	,
"	石臼	"	,
"	別荘	"	,
"	撹乳器	"	,
"	週末市場	"	,
"	糸巻き棒	"	,
"	水車	"	,
]



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

    if message.content.startswith("uranai"):
        if client.user != message.author:
            random.shuffle(list2)
            random.shuffle(list3)
            m = message.author.name + "さんの今日の運勢は" + list3[0] + "で"+ list2[0] + "を引くくらいの運勢です。"
            await message.channel.send(m)

    if message.content.startswith("card2"):
        if client.user != message.author:
            random.shuffle(list4)
            m = emoji.emojize(list4[0]+list4[1], use_aliases=True)
            await message.channel.send(m)

    if message.content.startswith("card1"):
        if client.user != message.author:
            random.shuffle(list4)
            m = emoji.emojize(list4[0], use_aliases=True)
            await message.channel.send(m)

    if message.content.startswith("card3"):
        if client.user != message.author:
            random.shuffle(list4)
            m = emoji.emojize(list4[0]+list4[1]+list4[2], use_aliases=True)
            await message.channel.send(m)

    if message.content.startswith("napo"):
        if client.user != message.author:
            random.shuffle(list5)
            m = emoji.emojize(list5[0]+list5[1]+list5[2]+list5[3]+list5[4]+list5[5]+list5[6]+list5[7]+list5[8]+list5[9], use_aliases=True)
            await message.channel.send(m)

    if message.content.startswith("pick"):
        if client.user != message.author:
            random.shuffle(listN)
            m = "左から" + str(listN[0]) + "番目をピックしましょう！"
            await message.channel.send(m)

    if message.content.startswith("hato"):
        if client.user != message.author:
            random.shuffle(list6)
            newlist6 = [list6[0], list6[1], list6[2],list6[3], list6[4], list6[5],list6[6], list6[7], list6[8], list6[9] ]
            newlist6.sort()
            m = "__ランダム10種__"+"\n"+"\n"+str(newlist6[0])+"\n"+str(newlist6[1])+"\n"+str(newlist6[2])+"\n"+str(newlist6[3])+"\n"+str(newlist6[4])+"\n"+str(newlist6[5])+"\n"+str(newlist6[6])+"\n"+str(newlist6[7])+"\n"+str(newlist6[8])+"\n"+str(newlist6[9])
            await message.channel.send(m)

    if message.content.startswith("ag3"):
        if client.user != message.author:
            random.shuffle(list7)
            random.shuffle(list8)
            m = message.author.name + "さんの束"+"\n"+"\n"+"__職業__"+"\n"+list7[0]+"・"+list7[1]+"・"+list7[2]+"・"+list7[3]+"・"+list7[4]+"・"+list7[5]+"・"+list7[6]+"\n"+"\n"+"__小進歩__"+"\n"+list8[0]+"・"+list8[1]+"・"+list8[2]+"・"+list8[3]+"・"+list8[4]+"・"+list8[5]+"・"+list8[6]
            await message.channel.send(m)

    if message.content.startswith("ping"):
        if client.user != message.author:
            m = "pong"
            await message.channel.send(m)

    if message.content.startswith("name"):
        if client.user != message.author:
            m = "Torisan"
            await message.channel.send(m)



client.run(token)
