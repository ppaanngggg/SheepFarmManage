create table chan_gao
(
	chan_gao_hao char(10) not null primary key,
	peng_hao char(5) not null,
	lan_hao char(5) not null,
	mu_yang_hao char(10) not null,
	gong_yang_hao char(10) not null,
	tai_ci int,
	pei_zhong_ri_qi date,
	chan_gao_ri_qi date not null,
	chan_gao int not null,
	huo_gao int not null,
	duan_nai_ri_qi date
);

create table yang
(
	bian_hao char(10) not null primary key,
	peng_hao char(5),
	lan_hao char(5),
	chan_gao_hao char(10) not null,
	xing_bie char(5) not null,
	er_hao char(10),
	mian_yi_hao char(10),
	chu_sheng_zhong float(10,1),
	duan_nai_zhong float(10,1),
	liu_yue_zhong float(10,1),
	zhou_sui_zhong float(10,1),
	qu_xiang char(20),
	chan_gao_bian_hao char(10)
);