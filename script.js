// ===== News Data =====
const staticNews = {
  finance: [
    { title: "月之暗面完成20亿美元新融资", summary: "估值突破200亿美元，成为AI领域超级独角兽", date: "5月7日", link: "https://36kr.com", image: "https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=800&q=80", detail: "月之暗面（Moonshot AI）即将完成新一轮20亿美元融资，本轮融资后公司估值将超过200亿美元，跻身全球AI独角兽前列。\n\n投资方包括腾讯、阿里巴巴等战略投资者以及多家头部美元基金。此前，月之暗面已完成多轮融资，累计融资额超过30亿美元。公司成立于2023年，由前清华大学研究人员杨植麟创立，专注于大语言模型研发。\n\n公司旗下Kimi智能助手月活已突破3000万，成为国内增长最快的AI应用之一。Kimi以其超长上下文窗口（支持200万字上下文）和出色的中文理解能力著称，在文档分析、代码辅助、内容创作等场景表现优异。本轮融资将主要用于模型训练、人才引进和商业化拓展。", badge: "热点" },
    { title: "李嘉诚抛售资产套现约455亿", summary: "持续优化资产结构，聚焦核心业务", date: "5月7日", link: "https://finance.sina.com.cn", image: "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800&q=80", detail: "李嘉诚家族通过旗下长和系公司近期完成多笔资产出售，累计套现约455亿港元，引发市场广泛关注。\n\n出售资产包括英国水务公司Northumbrian Water、欧洲港口资产以及亚洲部分地产项目。这是李嘉诚近年来最大规模的资产处置行动之一，显示出其对全球经济不确定性和地缘政治风险的谨慎态度。\n\n市场分析认为，这是李嘉诚一贯的反周期操作策略。在经济繁荣期积累资产，在不确定性增加时变现，将资金转向更安全的领域。近期，长和系公司的现金储备已达到历史高位，为未来可能出现的投资机会做好了准备。", badge: "" },
    { title: "宝马一季度利润降25%", summary: "至23亿欧元，受中国市场竞争加剧影响", date: "5月7日", link: "https://www.bmw.com", image: "https://images.unsplash.com/photo-1555212697-194d092e3b8f?w=800&q=80", detail: "宝马集团发布2025年第一季度财报，业绩表现不及市场预期。营收同比下降15.2%至366亿欧元，净利润下降25%至23亿欧元，毛利率也承压下行。\n\n中国作为宝马全球最大单一市场，销量下滑17.2%，成为拖累全球业绩的主要因素。比亚迪、蔚来、理想等本土电动车品牌通过激烈的价格战不断蚕食市场份额，宝马在传统燃油车领域的优势正在被削弱。\n\n为应对挑战，宝马宣布将在华推出更多纯电车型，包括全新iX3、i5等车型，并计划将沈阳生产基地的产能向新能源倾斜。同时，宝马加大了在自动驾驶和智能座舱领域的研发投入，试图通过技术创新重建竞争力。", badge: "" },
    { title: "壳牌启动30亿美元股票回购", summary: "第一季度调整后盈利69.15亿美元", date: "5月7日", link: "https://www.shell.com", image: "https://images.unsplash.com/photo-1611284446314-60a58ac0deb9?w=800&q=80", detail: "壳牌公布2026年第一季度财报，业绩大幅超出市场预期。调整后盈利达69.15亿美元，环比增长112%，主要得益于天然气和液化天然气业务的强劲表现。\n\n公司在财报中表示，全球能源转型背景下，壳牌的天然气业务成为稳定的现金流来源。同时，公司在可再生能源领域的投资也开始产生回报，风电和光伏项目的收益率持续改善。\n\n为回报股东，壳牌宣布启动未来三个月30亿美元的股票回购计划，并将季度股息提高5%至0.3906美元/股。这是壳牌连续第12个季度提高股息，显示出管理层对未来现金流的信心。分析师认为，壳牌正在成功实现从传统石油公司向综合能源公司的转型。", badge: "" },
    { title: "阿迪达斯有望获3亿欧元关税退款", summary: "根据美国最高法院关税裁决", date: "5月7日", link: "https://www.adidas-group.com", image: "https://images.unsplash.com/photo-1511556532299-8f662fc26c06?w=800&q=80", detail: "阿迪达斯首席执行官在年度股东大会上透露重磅消息：根据美国最高法院近期关税裁决，公司有望获得3亿欧元（约3.35亿美元）的美国关税退款。\n\n这笔资金来源于特朗普政府时期对欧洲商品征收的额外关税。当时阿迪达斯等欧洲品牌被迫承担额外成本，或将成本转嫁给消费者。阿迪达斯此前已在财报中计提了相关准备金，如果退款成功，将直接计入当期利润。\n\n古尔登表示，阿迪达斯在美国的销售占全球收入的约25%，关税政策的变化对公司的盈利能力有显著影响。此次最高法院的裁决可能为更多欧洲品牌争取到类似待遇，有助于缓解贸易摩擦对消费品行业的冲击。", badge: "" },
    { title: "英监管机构调查支付三巨头垄断", summary: "PayPal、万事达、Visa涉嫌反竞争行为", date: "5月7日", link: "https://www.fca.org.uk", image: "https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=800&q=80", detail: "英国金融行为监管局（FCA）宣布对美国三大支付巨头PayPal、万事达卡和Visa启动反垄断调查，震动了全球支付行业。\n\n调查重点关注PayPal数字钱包的相关行为是否涉嫌反竞争，特别是PayPal与万事达、Visa之间的合作安排是否限制了市场竞争。去年发布的数字钱包行业报告揭示了这些支付巨头在数字钱包市场的 dominance，引发了监管机构的担忧。\n\n如果调查认定存在垄断行为，三家公司可能面临高额罚款，甚至被要求调整商业模式。这将对全球数字支付市场产生深远影响，也可能促使更多新兴支付公司进入市场，增加竞争活力。", badge: "" },
    { title: "贵州茅台4月回购28.91万股", summary: "支付金额4.09亿元，累计回购15.21亿元", date: "5月7日", link: "https://www.moutaichina.com", image: "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=800&q=80", detail: "贵州茅台发布回购股份进展公告，显示公司正在稳步推进股票回购计划。2026年4月累计回购股份28.91万股，支付金额4.09亿元。\n\n截至4月底，公司已累计回购股份108.33万股，占总股本0.0865%，已支付总金额15.21亿元（不含交易费用）。本次回购的股份将用于注销并减少注册资本，而非员工持股计划。\n\n茅台的回购计划是在股价承压背景下推出的。2026年以来，白酒行业整体面临消费疲软的压力，茅台股价较年初高点有所回落。通过回购注销，公司希望向市场传递对未来发展的信心，同时提升每股收益。市场分析师认为，茅台的现金流充裕，回购计划仍有较大的执行空间。", badge: "" },
    { title: "WTI原油跌破90美元/桶", summary: "日内下跌超5%，能源市场波动加剧", date: "5月7日", link: "https://www.eia.gov", image: "https://images.unsplash.com/photo-1519810755548-39cd217da494?w=800&q=80", detail: "WTI原油期货价格向下跌破90美元/桶关口，报89.93美元/桶，日内跌幅达5.41%，创下近三个月最大单日跌幅。\n\n油价暴跌主要受三重因素影响：一是美国原油库存超预期增加，EIA数据显示上周库存增加超过500万桶；二是OPEC+可能在即将召开的会议上宣布增产，以应对市场份额流失；三是全球经济增长担忧升温，美国一季度GDP增速低于预期，中国制造业PMI也显示复苏乏力。\n\n布伦特原油同步下跌至93美元/桶附近，能源板块股票普跌。埃克森美孚、雪佛龙等能源巨头股价跌幅超过3%。分析师认为，如果全球经济数据继续疲软，油价可能进一步下探85美元/桶支撑位。", badge: "" }
  ],
  tech: [
    { title: "AI视频Agent赛道爆发", summary: "头部平台月算力消耗百万级，ARR可达2000万美元。但面临大厂模型层碾压风险", date: "36氪深度 · 5月7日", link: "https://36kr.com", image: "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800&q=80", detail: "AI视频生成赛道正在经历大厂模型能力疯狂增长的巨大红利期。来自字节跳动的Seedance和快手的可灵这两款超级底座正在进行一周一小版、两月一大版的高频迭代，技术能力快速逼近专业影视制作水准。\n\n众多短剧、内容公司排队等待使用最新版模型已成为行业奇观。由此，在AI视频模型外套一层壳使其更简单易上手的AI视频Agent产品迎来增长奇迹。头部平台月算力消耗达百万元级别，ARR可达2000万美元。\n\n但创业公司也面临巨大挑战：如果大厂从模型层走到应用层，跟自己抢饭碗怎么办？业内判断，大厂会做但不会明天就做，这个窗口期可能还有3-5年。创业公司的护城河在于更早跑起来形成的用户留存与数据沉淀，以及越来越深的业务服务能力。", badge: "重磅" },
    { title: "腾讯、百度入股机器人灵巧手研发商", summary: "投资临界点公司，智元机器人拆分业务独立发展", date: "5月7日", link: "https://36kr.com", image: "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&q=80", detail: "上海临界点创新智能科技有限公司近日发生工商变更，新增腾讯旗下上海启善投资有限公司、百度旗下三亚百川致新私募股权投资基金等重量级股东，注册资本由约554万人民币增至约597万人民币。\n\n该公司成立于2026年1月，由智元机器人将其灵巧手业务拆分而独立成立，是一家专注于机器人末端执行器，特别是灵巧手研发与生产的全球化科技公司。法定代表人为王闯，经营范围包括人工智能硬件销售、智能机器人销售及研发等。\n\n灵巧手被称为机器人的末端执行器，是实现精细化操作的关键部件。腾讯和百度的入局，显示出科技巨头对机器人产业链上游核心零部件的高度重视。随着人形机器人产业化加速，灵巧手市场规模预计将在未来五年内突破百亿元。", badge: "" },
    { title: "宇树UniStore全面开放", summary: "全球首个人形机器人任务动作应用商店上线", date: "5月7日", link: "https://www.unitree.com", image: "https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=800&q=80", detail: "宇树科技宣布UniStore官方共享应用平台正式全面开放，这是全球首个人形机器人任务动作应用商店，标志着机器人软件生态建设迈出重要一步。\n\n开发者可以在平台上发布和销售机器人动作程序，用户可直接下载到宇树Go2、H1等人形机器人上执行。平台首批上线超过200个任务动作包，涵盖舞蹈、武术、搬运、巡检等多种场景。\n\nUniStore的推出借鉴了苹果App Store和Steam的模式，试图通过开放生态吸引更多开发者参与。宇树科技表示，平台将提供完善的分成机制，开发者可获得70%的收入。业内专家认为，硬件标准化加软件生态开放，是消费级机器人走向普及的必经之路。", badge: "" },
    { title: "Neuralink研发大脑手术机器人", summary: "目标是开发通用神经接口，解决所有大脑相关疾病", date: "5月6日", link: "https://neuralink.com", image: "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=800&q=80", detail: "当地时间5月6日，马斯克旗下脑机接口公司Neuralink发文称，正在研发一种能够到达大脑任何区域的手术机器人，目标是开发一种通用的神经接口，以帮助解决所有源于大脑的疾病。\n\nNeuralink表示，目前的脑机接口设备主要用于运动皮层，而新的手术机器人将能够到达大脑的任何区域，包括深部脑区。这将大大扩展脑机接口的适用范围，从运动障碍扩展到抑郁症、癫痫、帕金森病等更多神经系统疾病。\n\n设备目前处于研究阶段，尚未获得FDA批准。Neuralink此前已完成首例人体植入，受试者是一名四肢瘫痪的患者，通过脑机接口成功实现了意念控制电脑光标。公司计划在2026年内完成10例人体植入。", badge: "" },
    { title: "千问PC端上线AI语音输入", summary: "阿里大模型产品持续迭代升级", date: "5月7日", link: "https://tongyi.aliyun.com", image: "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&q=80", detail: "阿里云旗下大模型产品千问（Qwen）PC端正式上线AI语音输入功能，进一步降低了人机交互的门槛。该功能支持普通话、英语及粤语、四川话等多种方言识别，识别准确率超过95%。\n\n用户可通过语音直接与AI助手交互，无需键盘输入，特别适合办公场景下的快速记录和创意发散。除了语音输入，本次更新还包括文档解析能力提升，支持PDF、Word、Excel等多种格式的深度解析，以及代码生成优化，支持超过100种编程语言。\n\n千问系列模型目前已迭代至3.0版本，在多项国际评测中名列前茅。阿里表示，语音交互是AI助手普及的关键路径，未来将不断优化语音识别的准确率和响应速度，让AI助手像真人助手一样自然交流。", badge: "" },
    { title: "重庆出台L3级自动驾驶测试新规", summary: "规范高速公路场景，加速商业化落地", date: "5月7日", link: "https://www.cq.gov.cn", image: "https://images.unsplash.com/photo-1617788138017-80ad40651399?w=800&q=80", detail: "重庆市经济信息委联合市公安局、市交委近日印发《重庆市智能网联汽车高速公路测试管理细则（试行）》，这是国内首个专门针对L3级及以上智能网联汽车高速公路测试的规范性文件。\n\n细则进一步补齐高阶自动驾驶高速场景测试制度短板，对测试主体、测试车辆、测试人员、测试流程、数据记录和事故处理等全流程进行了详细规定。特别明确了L3级自动驾驶在高速公路场景下的权责划分，要求测试主体必须购买不低于500万元的交通事故责任保险。\n\n重庆是国内智能网联汽车产业发展的重镇，拥有长安、赛力斯等头部车企。此次新规的出台，为自动驾驶技术的商业化落地扫清了制度障碍。业内预计，到2027年，重庆将建成超过500公里的智能网联汽车开放测试道路。", badge: "" },
    { title: "智源发布心脏磁共振诊断智能体", summary: "BAAI Cardiac Agent，业内首个多模态诊断AI", date: "5月6日", link: "https://www.baai.ac.cn", image: "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&q=80", detail: "北京智源人工智能研究院（BAAI）发布业内首个心脏磁共振多模态诊断智能体BAAI Cardiac Agent，开创了AI辅助心脏疾病诊断的新范式。\n\n该系统采用多模态融合架构，可同时处理心脏MRI影像、患者病史文本和结构化检验数据，自动生成包含病灶定位、定量分析和诊断建议的完整报告。在内部测试中，该系统对心肌缺血、心肌梗死、心肌病等常见心脏疾病的诊断准确率接近资深影像科医生水平。\n\n智源研究院表示，BAAI Cardiac Agent的核心技术在于跨模态注意力机制，能够自动关联影像特征和临床数据，减少漏诊和误诊。目前该系统已进入多家三甲医院开展临床验证，预计2026年下半年申请医疗器械注册证。", badge: "" }
  ],
  products: [
    { title: "三星退出中国家电市场", summary: "宣布停止在中国大陆销售所有家电产品", date: "5月7日", link: "https://news.samsung.com", image: "https://images.unsplash.com/photo-1550009158-9ebf69173e03?w=800&q=80", detail: "三星电子正式宣布停止在中国大陆市场销售所有家电产品，包括冰箱、洗衣机、空调、电视等全线白电及黑电产品。这一决定标志着三星在中国消费电子市场的全面撤退。\n\n公司表示未来将聚焦手机、半导体、显示面板等核心业务在华发展。事实上，三星在中国的家电业务近年来持续萎缩，市场份额已被海尔、美的、格力等本土品牌远远甩在身后。在高端市场，索尼、博西家电（博世+西门子）也占据了更有利的位置。\n\n回顾三星的在华历程，公司曾在2019年关闭惠州手机工厂，将制造业务转移到越南和印度。如今家电业务的退出，是三星全球化战略调整的最新一步。分析师认为，中国家电市场竞争异常激烈，价格战频繁，外资品牌盈利空间被严重压缩，退出是理性的商业决策。", badge: "重大" },
    { title: "一加 Ace 6 至尊版发布", summary: "定位颗秒神器，性能操控赛旗舰", date: "5月6日", link: "https://www.oneplus.com", image: "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=800&q=80", detail: "一加正式发布Ace 6至尊版手机，这款手机被官方定位为颗秒神器，主打极致性能和游戏体验。核心配置方面，搭载骁龙8至尊版处理器，配备120Hz LTPO自适应刷新率屏幕和5400mAh大电池，支持100W超级闪充。\n\n游戏体验是这款手机的最大亮点。一加为其搭载了超帧超画引擎，通过AI算法将游戏帧率提升至120帧，同时增强画面细节。官方表示，目前已有超过100款主流游戏支持该功能，包括《王者荣耀》《和平精英》《原神》等。\n\n起售价2999元（12+256GB版本），定位中高端性能旗舰。一加表示，Ace系列的使命是为追求极致性能的用户提供高性价比选择，与数字系列形成互补。该机型将于5月15日首销。", badge: "" },
    { title: "xTool发布彩色打印+激光切割新品", summary: "二合一设计，创客工具新选择", date: "5月7日", link: "https://xtool.com", image: "https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?w=800&q=80", detail: "xTool发布新款桌面级创客工具M1 Ultra，创新性地将彩色喷墨打印与激光切割功能集成到一台设备中，填补了市场上多功能创客工具的空白。\n\n该设备支持在木材、皮革、亚克力、布料等多种材料上先打印彩色图案，再通过激光精确切割，实现从设计到成品的全流程制作。打印分辨率可达1200dpi，激光切割精度为0.01mm，足以满足大多数创客项目的需求。\n\n产品定位教育机构和DIY爱好者市场，售价6999元起。xTool表示，随着STEAM教育的普及，学校和家庭对多功能创作工具的需求正在快速增长。M1 Ultra的推出，让创作者无需购买多台设备即可完成复杂作品，大大降低了创客门槛。", badge: "" },
    { title: "vivo Pad6 Pro发布", summary: "4K原彩屏+骁龙8至尊版，旗舰平板新标杆", date: "5月4日", link: "https://www.vivo.com", image: "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=800&q=80", detail: "vivo发布Pad6 Pro旗舰平板电脑，这是vivo在平板领域的全新旗舰之作，明确瞄准生产力工具和创意创作市场。\n\n硬件配置方面，配备13英寸4K原彩显示屏，支持HDR10+和120Hz刷新率；搭载骁龙8至尊版芯片，性能媲美旗舰手机；内置PC级WPS Office和专业版剪映，满足移动办公和视频剪辑需求。电池容量高达11500mAh，支持66W快充，官方称可连续播放视频超过12小时。\n\n起售价3999元（8+128GB版本），将于5月15日开售。vivo表示，Pad6 Pro的目标是成为安卓平板中的iPad Pro挑战者，通过强大的硬件和优化的软件生态，吸引商务人士和创意工作者。同时，vivo还推出了配套的智能键盘和触控笔，进一步完善生产力体验。", badge: "" },
    { title: "Apple和解Siri延期集体诉讼", summary: "同意支付和解金，避免长期法律纠纷", date: "5月7日", link: "https://www.apple.com", image: "https://images.unsplash.com/photo-1491933382434-500287f9b54b?w=800&q=80", detail: "苹果公司同意就Siri语音助手隐私诉讼达成和解，同意支付9500万美元和解金。这场集体诉讼始于2019年，当时媒体报道称苹果雇佣的承包商在审查Siri录音时，听到了用户的私人对话，包括医疗信息、商业交易甚至夫妻生活。\n\n诉讼指控苹果在未经用户明确同意的情况下，通过Siri记录用户对话并分享给第三方承包商用于质量审核。原告认为这侵犯了用户的隐私权。苹果否认存在不当行为，但选择和解以避免旷日持久的诉讼带来的声誉损失和不确定性。\n\n根据和解协议，9500万美元将用于赔偿在2014年至2024年间使用Siri的美国用户，预计每位用户可获得约20美元赔偿。苹果还承诺永久删除2019年10月之前收集的所有Siri录音，并改进隐私政策，明确告知用户语音数据的用途。", badge: "" },
    { title: "Valve开源Steam Controller CAD文件", summary: "外壳设计文件开放，社区可3D打印替换件", date: "5月7日", link: "https://store.steampowered.com", image: "https://images.unsplash.com/photo-1592840496694-26d035b52b48?w=800&q=80", detail: "Valve公司宣布开源Steam Controller游戏手柄的外壳CAD设计文件，采用知识共享署名许可协议（CC BY 4.0）。这意味着任何用户都可以免费下载、修改和重新分发这些设计文件。\n\nSteam Controller是Valve在2015年推出的创新型游戏手柄，以其双触控板替代传统摇杆的设计而闻名。虽然该手柄已于2019年停产，但由于其独特的输入方式和高度可定制性，仍在核心玩家群体中拥有大量忠实用户。\n\n开源CAD文件后，社区用户可以3D打印替换外壳、修复损坏部件，甚至设计全新的外观。这在游戏硬件领域是一个罕见的举措，显示出Valve对社区创新的支持。目前文件已上传至GitHub，包含外壳、握把和按键的完整3D模型，兼容主流3D打印格式。", badge: "" }
  ],
  auto: [
    { title: "巴西5月11日起对中国公民免签", summary: "每次入境最长可停留30天，赴巴西机票搜索量猛增", date: "5月7日", link: "https://www.gov.br", image: "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=800&q=80", detail: "巴西政府5月7日正式宣布，自2026年5月11日起，对持普通护照的中国公民实施免签入境政策。根据巴西外交部发布的公报，持普通护照的中华人民共和国公民可享受短期免签入境，每次入境最长可停留30天。\n\n消息发布后，中国旅游市场反应热烈。去哪儿旅行指数显示，截至5月7日晚8点半，飞赴巴西里约热内卢搜索量环比上一小时翻倍，环比上周增近2倍；飞赴巴西利亚机票搜索量环比前一小时增2倍，环比上周大增4.5倍。\n\n巴西是南美洲最大的国家，拥有里约热内卢、亚马逊雨林、伊瓜苏瀑布等世界级旅游资源。此前中国公民赴巴西需办理签证，流程相对繁琐。免签政策的实施，预计将大幅提升中国游客赴南美旅游的热情，也有望带动中巴之间的商务往来。", badge: "免签" },
    { title: "本田叫停加拿大电动汽车工厂计划", summary: "美国市场需求疲软，原定2028年开工项目无限期冻结", date: "5月6日", link: "https://global.honda", image: "https://images.unsplash.com/photo-1550009158-9ebf69173e03?w=800&q=80", detail: "本田汽车公司决定无限期冻结在加拿大建设电动汽车工厂的计划，这是全球汽车产业电动化转型遇阻的最新信号。该项目连同配套电池工厂总计投资150亿加元（约110亿美元），原定于2028年开工。\n\n本田做出这一决定的直接原因是美国市场需求疲软。2026年第一季度，本田在美国市场的电动车销量仅为预期的60%，库存积压严重。同时，美国政策环境的不确定性——包括可能的关税调整和补贴政策变化——也让本田对未来的投资回报产生疑虑。\n\n值得注意的是，本田去年已将开工日期延后两年，如今彻底叫停。这一决定不仅影响本田自身的电动化战略，也对加拿大的汽车产业链造成冲击。安大略省政府此前已为该项目提供了超过10亿加元的税收优惠和基础设施支持。", badge: "" },
    { title: "江铃汽车4月销量增长14.59%", summary: "4月销售34948辆，本年累计增长13.62%", date: "5月7日", link: "https://www.jmc.com.cn", image: "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?w=800&q=80", detail: "江铃汽车公告2026年4月销量数据，展现出稳健的增长态势。4月销售34948辆，同比增长14.59%；本年累计销量121013辆，同比增长13.62%，在行业整体承压的背景下表现亮眼。\n\n增长主要来自轻客和皮卡业务。江铃福特全顺系列轻客继续在商用面包车市场保持领先地位，福特Ranger皮卡在户外越野爱好者中口碑良好。新能源方面，江铃纯电动轻客和皮卡销量占比已提升至18.5%，高于行业平均水平。\n\n江铃汽车表示，2026年公司将继续推进新能源战略，计划推出多款插电混动和纯电动新车型。同时，公司也在积极拓展海外市场，特别是在东南亚和南美地区，江铃商用车凭借性价比优势获得了不错的市场反响。", badge: "" },
    { title: "飞猪五一数据亮眼", summary: "88VIP履约酒店间夜量同比增长超100%", date: "5月7日", link: "https://www.fliggy.com", image: "https://images.unsplash.com/photo-1531746790731-6c087fecd65a?w=800&q=80", detail: "飞猪发布2026年五一假期（5月1日-5日）旅游数据，多项指标创历史新高，显示出中国旅游市场强劲的复苏势头。\n\n酒店业务方面，单日成交间夜量再次破历史峰值。其中88VIP会员贡献的酒店实际履约间夜量同比增长超100%，显示出高价值用户的消费力持续释放。高端酒店和精品民宿的增长尤为显著，同比增幅分别达到150%和180%，反映出消费者对高品质住宿体验的追求。\n\n出境游方面，日本、泰国、新加坡位居热门目的地前三。受益于签证便利化政策和航班恢复，日本游热度超过疫情前水平。此外，小众目的地如格鲁吉亚、乌兹别克斯坦、摩洛哥等也进入增速前十，显示出中国游客对差异化体验的需求正在增长。", badge: "" },
    { title: "去哪儿：赴巴西机票搜索量猛增", summary: "里约热内卢环比增近2倍，巴西利亚环比增4.5倍", date: "5月7日", link: "https://www.qunar.com", image: "https://images.unsplash.com/photo-1526392060635-9d6019884377?w=800&q=80", detail: "去哪儿旅行指数显示，巴西免签消息发布后，赴巴西机票搜索量出现爆发式增长。飞赴里约热内卢的搜索量环比前一小时翻倍，环比上周增近2倍；飞赴巴西利亚的搜索量环比前一小时增2倍，环比上周大增4.5倍。\n\n南美游有望成为今年出境游的新热点。除了巴西，阿根廷、智利等国也对中国游客推出便利化措施。去哪儿数据显示，五一期间南美整体搜索量已较年初增长超过300%，虽然基数较小，但增速惊人。\n\n业内专家指出，南美旅游资源丰富且独特，但长期以来受限于距离遥远（飞行时间超过20小时）和签证门槛。随着航线增加和签证政策放宽，预计2026年下半年将有更多中国游客踏上南美之旅。目前，国航、南航已计划增加北京-圣保罗、广州-里约热内卢的航班频次。", badge: "" }
  ],
  vc: [
    { title: "像素绽放PixelBloom完成C轮融资", summary: "全面发力AI办公Agent，从一分钟生成PPT到交付商用级结果", date: "5月7日", link: "https://36kr.com", image: "https://images.unsplash.com/photo-1551434678-e076c223a692?w=800&q=80", detail: "AI办公解决方案公司像素绽放PixelBloom完成C轮融资，投资方包括红杉中国和多家知名美元基金。本轮融资后，公司将全面发力AI办公Agent方向，从内容生成拓展到商用交付的全流程解决方案。\n\n像素绽放此前以AI生成PPT工具Pixso和AiPPT闻名，用户量已突破千万。其产品可在1分钟内根据用户输入的主题自动生成完整PPT，包括大纲、配图和排版。在2025年，公司进一步推出了AI数据分析报告、AI合同审查等办公场景应用。\n\n新融资将重点用于三个方面：一是扩充Agent产品矩阵，覆盖更多办公场景；二是建立企业级服务团队，为大客户提供定制化交付；三是拓展海外市场，特别是东南亚和中东地区。创始人表示，AI办公Agent的目标是让每个职场人拥有专属的AI助理，将重复性工作效率提升10倍以上。", badge: "融资" },
    { title: "LiblibAI完成1.3亿美元B轮融资", summary: "红杉中国、CMC资本投资，一年内连续四轮融资", date: "5月7日", link: "https://36kr.com", image: "https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=800&q=80", detail: "AI视频创作平台LibTV母公司LiblibAI在去年10月完成由红杉中国、CMC资本等机构投资的1.3亿美元B轮融资，创下一年内连续四轮融资的行业纪录，成为2025年创投市场最活跃的公司之一。\n\nLiblibAI的核心产品LibTV是一个AI驱动的视频创作平台，用户可以通过自然语言描述生成短视频、广告片和动画内容。平台集成了文本生成、图像生成和视频生成等多种AI能力，创作者无需专业技能即可制作高质量视频。\n\n完成B轮融资后，母公司估值超过10亿美元，跻身AI视频赛道独角兽行列。公司表示，资金将主要用于模型训练、算力扩充和海外市场拓展。目前LibTV的海外版已在美国和欧洲上线，月活用户超过500万。竞争对手包括Runway、Pika Labs等国际知名AI视频公司。", badge: "" },
    { title: "斯坦福博士后柔性触觉传感器公司获超亿元融资", summary: "低成本触觉手套即将量产落地", date: "5月7日", link: "https://36kr.com", image: "https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?w=800&q=80", detail: "由斯坦福博士后创立的柔性触觉传感器公司完成超亿元Pre-A轮融资，投资方包括高瓴创投、经纬中国等知名机构。这一融资规模在硬科技早期项目中较为罕见，显示出资本市场对触觉传感器赛道的高度认可。\n\n公司研发的低成本柔性触觉手套采用新型导电聚合物材料，可实现亚毫米级空间分辨率和毫秒级响应速度，性能接近人类手指的触觉感知能力。与进口同类产品相比，成本降低超过70%，具备大规模商用条件。\n\n应用场景包括机器人灵巧操作、VR/AR触觉反馈、假肢控制等。公司已与多家机器人厂商和VR设备商达成合作意向，预计2026年下半年实现量产。创始人表示，触觉是机器人实现精细化操作的最后一块拼图，随着人形机器人产业化加速，触觉传感器市场将迎来爆发式增长。", badge: "" },
    { title: "林清轩年入25亿", summary: "创始人孙来春表示不想做中国欧莱雅", date: "5月7日", link: "https://36kr.com", image: "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=800&q=80", detail: "国产高端护肤品牌林清轩创始人孙来春在专访中透露，公司年收入已达25亿元。他表示林清轩的目标是成为'林清轩自己'，而非'中国的欧莱雅'。品牌以山茶花护肤油为核心单品，在全国拥有超过600家门店。", badge: "" }
  ]
};
let dynamicNews = {};

// ===== Load Data =====
async function loadNewsData() {
  try {
    const response = await fetch('news-data.json');
    if (response.ok) {
      dynamicNews = await response.json();
    }
  } catch (e) {
    console.log('Using static news data');
  }
  
  // Merge dynamic news into static
  const medicalNews = (dynamicNews.medical || []).map(n => ({...n, badge: n.badge || ''}));
  const educationNews = (dynamicNews.education || []).map(n => ({...n, badge: n.badge || ''}));
  const aerospaceNews = (dynamicNews.aerospace || []).map(n => ({...n, badge: n.badge || ''}));
  
  renderSection('finance-grid', staticNews.finance);
  renderSection('tech-grid', staticNews.tech);
  renderSection('products-grid', staticNews.products);
  renderSection('auto-grid', staticNews.auto);
  renderSection('vc-grid', staticNews.vc);
  renderSection('medical-grid', medicalNews);
  renderSection('education-grid', educationNews);
  renderSection('aerospace-grid', aerospaceNews);
}

// ===== Event Delegation for Cards =====
function setupCardEvents() {
  document.querySelectorAll('.news-card').forEach(card => {
    // Get grid id and index from onclick attribute if present
    const onclickAttr = card.getAttribute('onclick');
    if (onclickAttr) {
      const match = onclickAttr.match(/openModal\('([^']+)',\s*(\d+)\)/);
      if (match) {
        card.dataset.grid = match[1];
        card.dataset.index = match[2];
        card.removeAttribute('onclick');
      }
    }
    
    card.addEventListener('click', function(e) {
      e.preventDefault();
      const gridId = this.dataset.grid;
      const index = parseInt(this.dataset.index);
      if (gridId && !isNaN(index)) {
        openModal(gridId, index);
      }
    });
  });
}

// ===== Render Section =====
const sectionGradients = {
  'finance-grid': { gradient: 'linear-gradient(135deg, #00d4ff, #7c3aed)', emoji: '💰' },
  'tech-grid': { gradient: 'linear-gradient(135deg, #00ff88, #00d4ff)', emoji: '🤖' },
  'products-grid': { gradient: 'linear-gradient(135deg, #ff6b35, #ff0080)', emoji: '📱' },
  'auto-grid': { gradient: 'linear-gradient(135deg, #ff9500, #ff0040)', emoji: '🚗' },
  'vc-grid': { gradient: 'linear-gradient(135deg, #a855f7, #ec4899)', emoji: '🏢' },
  'medical-grid': { gradient: 'linear-gradient(135deg, #00d4ff, #00ff88)', emoji: '🏥' },
  'education-grid': { gradient: 'linear-gradient(135deg, #f59e0b, #ff6b35)', emoji: '📚' },
  'aerospace-grid': { gradient: 'linear-gradient(135deg, #3b82f6, #8b5cf6)', emoji: '🚀' }
};

function renderSection(gridId, items) {
  const grid = document.getElementById(gridId);
  if (!grid || !items || !items.length === 0) return;
  
  const theme = sectionGradients[gridId] || { gradient: 'linear-gradient(135deg, #00d4ff, #7c3aed)', emoji: '📰' };
  
  grid.innerHTML = items.map((item, index) => `
    <article class="news-card ${index === 0 ? 'featured' : ''}" onclick="openModal('${gridId}', ${index})">
      <div class="card-image-wrapper">
        ${item.image ? `<img src="${item.image}" alt="${item.title}" class="card-image" loading="lazy">` : `<div class="card-image-placeholder" style="background: ${theme.gradient}"><span class="card-emoji">${theme.emoji}</span></div>`}
        ${item.badge ? `<div class="card-badge ${item.badge === '热点' || item.badge === '重磅' ? 'hot' : item.badge === '融资' || item.badge === '免签' ? 'new' : ''}">${item.badge}</div>` : ''}
      </div>
      <div class="card-content">
        <h3>${item.title}</h3>
        <p>${item.summary}</p>
        <div class="card-meta">
          <span>${item.source || '资讯'} · ${item.date}</span>
          <span class="card-link">
            查看详情
            <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
              <path d="M6 12L10 8L6 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </span>
        </div>
      </div>
    </article>
  `).join('');
}

// ===== Modal =====
let currentNews = {};

function openModal(gridId, index) {
  let items;
  if (gridId === 'finance-grid') items = staticNews.finance;
  else if (gridId === 'tech-grid') items = staticNews.tech;
  else if (gridId === 'products-grid') items = staticNews.products;
  else if (gridId === 'auto-grid') items = staticNews.auto;
  else if (gridId === 'vc-grid') items = staticNews.vc;
  else if (gridId === 'medical-grid') items = dynamicNews.medical || [];
  else if (gridId === 'education-grid') items = dynamicNews.education || [];
  else if (gridId === 'aerospace-grid') items = dynamicNews.aerospace || [];
  
  const item = items[index];
  if (!item) return;
  
  currentNews = item;
  const theme = sectionGradients[gridId] || { gradient: 'linear-gradient(135deg, #00d4ff, #7c3aed)', emoji: '📰' };
  
  document.getElementById('modal-image').src = item.image || '';
  document.getElementById('modal-image').alt = item.title;
  const imgWrapper = document.getElementById('modal-image').parentElement;
  if (!item.image) {
    imgWrapper.style.background = theme.gradient;
    imgWrapper.innerHTML = `<div style="display:flex;align-items:center;justify-content:center;height:100%;"><span style="font-size:80px;">${theme.emoji}</span></div>`;
  } else {
    imgWrapper.style.background = '';
    imgWrapper.innerHTML = '<img src="" alt="" class="modal-image" id="modal-image">';
    document.getElementById('modal-image').src = item.image;
    document.getElementById('modal-image').alt = item.title;
  }
  document.getElementById('modal-title').textContent = item.title;
  document.getElementById('modal-meta').textContent = `${item.source || '资讯来源'} · ${item.date}`;
  document.getElementById('modal-body').innerHTML = (item.detail || item.summary).replace(/\n\n/g, '</p><p>').replace(/\n/g, '<br>');
  document.getElementById('modal-link').href = item.link || '#';
  document.getElementById('modal-badge').textContent = item.badge || '新闻';
  
  const overlay = document.getElementById('modal-overlay');
  overlay.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeModal(event) {
  if (event && event.target !== event.currentTarget) return;
  
  const overlay = document.getElementById('modal-overlay');
  overlay.classList.remove('active');
  document.body.style.overflow = '';
}

// Keyboard escape to close modal
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeModal();
});

// ===== Scroll Animations =====
const observerOptions = {
  root: null,
  rootMargin: '0px',
  threshold: 0.1
};

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, observerOptions);

document.querySelectorAll('.news-section').forEach(section => {
  sectionObserver.observe(section);
});



// ===== Active Nav Link =====
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-links a');

window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(section => {
    const sectionTop = section.offsetTop;
    if (scrollY >= sectionTop - 200) {
      current = section.getAttribute('id');
    }
  });
  
  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === `#${current}`) {
      link.classList.add('active');
    }
  });
});

// ===== Parallax Hero =====
window.addEventListener('scroll', () => {
  const scrolled = window.pageYOffset;
  const hero = document.querySelector('.hero-content');
  if (hero && scrolled < window.innerHeight) {
    hero.style.transform = `translateY(${scrolled * 0.3}px)`;
    hero.style.opacity = 1 - (scrolled / window.innerHeight) * 0.5;
  }
});

// ===== Navbar Shadow =====
window.addEventListener('scroll', () => {
  const navbar = document.querySelector('.navbar');
  if (window.scrollY > 50) {
    navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.08)';
  } else {
    navbar.style.boxShadow = 'none';
  }
});

// ===== Theme Toggle - Fixed for Feishu Browser =====
function initThemeToggle() {
  const btn = document.getElementById('themeToggle') || document.querySelector('.theme-toggle');
  if (!btn) return;
  
  // Remove any existing onclick
  btn.removeAttribute('onclick');
  
  // Set initial theme - default to dark (cyberpunk style)
  const html = document.documentElement;
  const currentTheme = html.getAttribute('data-theme') || 'dark';
  html.setAttribute('data-theme', currentTheme);
  btn.textContent = currentTheme === 'dark' ? '☀️' : '🌙';
  
  btn.addEventListener('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    
    const current = html.getAttribute('data-theme') || 'dark';
    const newTheme = current === 'dark' ? 'light' : 'dark';
    
    html.setAttribute('data-theme', newTheme);
    this.textContent = newTheme === 'dark' ? '☀️' : '🌙';
    
    // Try localStorage but don't fail if blocked
    try {
      localStorage.setItem('theme', newTheme);
    } catch (err) {
      console.log('localStorage not available');
    }
  });
}

// ===== Initialize =====
document.addEventListener('DOMContentLoaded', () => {
  initThemeToggle();
  setupCardEvents();
});

console.log('🎉 今日资讯网站 v2.0 已加载完成！');
console.log('📅 2025年5月8日 · 9大行业 · 45+精选资讯');
