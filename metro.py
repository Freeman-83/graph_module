from routing_module.base_classes import Node, Link, Graph


class Station(Node):
    ...


class LinkMetro(Link):
    ...


class TransferStation(Link):
    ...


class MetroGraph(Graph):
    ...


map_metro = MetroGraph()

# Ветки метро:

# фиолетовая:
v1 = Station("Планерная")
v2 = Station("Сходненская")
v3 = Station("Тушинская")
v4 = Station("Щукинская")
v5 = Station("Октябрьское поле")
v6 = Station("Полежаевсквая")
v7 = Station("Беговая")
v8 = Station("Улица 1905 года")
v9 = Station("Баррикадная")
v10 = Station("Пушкинская")
v11 = Station("Кузнецкий мост")
v12 = Station("Китай город (фиолетовая)")
v13 = Station("Таганская (радиальная)")
v14 = Station("Пролетарская")
v15 = Station("Волгоградский проспект")
v16 = Station("Текстильщики")
v17 = Station("Кузьминки")
v18 = Station("Рязанский проспект")
v19 = Station("Выхино")

# темно-зеленая:
v20 = Station("Речной вокзал")
v21 = Station("Водный стадион")
v22 = Station("Войковская")
v23 = Station("Сокол")
v24 = Station("Аэропорт")
v25 = Station("Динамо")
v26 = Station("Белорусская (радиальная)")
v27 = Station("Тверская")
v28 = Station("Театральная")
v29 = Station("Новокузнецкая")
v30 = Station("Павелецкая (радиальная)")
v31 = Station("Автозаводская")
v32 = Station("Коломенская")
v33 = Station("Каширская (темно-зеленая)")
v34 = Station("Кантемировская")
v35 = Station("Царицино")
v36 = Station("Орехово")
v37 = Station("Домодедовская")
v38 = Station("Красногвардейская")
v39 = Station("Маяковская")

# серая ветка:
v40 = Station("Алтуфьево")
v41 = Station("Бибирево")
v42 = Station("Отрадное")
v43 = Station("Владыкино")
v44 = Station("Петровско-разумовская")
v45 = Station("Тимирязевская")
v46 = Station("Дмитровская")
v47 = Station("Савеловская")
v48 = Station("Новослободская (радиальная)")
v49 = Station("Цветной бульвар")
v50 = Station("Чеховская")
v51 = Station("Боровицкая")
v52 = Station("Полянка")
v53 = Station("Серпуховская")
v54 = Station("Тульская")
v55 = Station("Нагатинская")
v56 = Station("Нагорная")
v57 = Station("Нахимовский проспект")
v58 = Station("Севастопольская")
v59 = Station("Чертановская")
v60 = Station("Южная")
v61 = Station("Пражская")
v62 = Station("Академика Янгеля")
v63 = Station("Анино")
v64 = Station("Бульвар Дмитрия Донского")

# оранжевая ветка:
v65 = Station("Медведково")
v66 = Station("Бабушкинская")
v67 = Station("Свиблово")
v68 = Station("Ботанический сад")
v69 = Station("ВДНХ")
v70 = Station("Алексеевская")
v71 = Station("Рижская")
v72 = Station("Проспект мира")
v73 = Station("Сухаревская")
v74 = Station("Тургеневская")
v75 = Station("Китай-Город (оранжевая)")
v76 = Station("Третьяковская (оранжевая)")
v77 = Station("Октябрьская (радиальная)")
v78 = Station("Шаболовская")
v79 = Station("Ленинский проспект")
v80 = Station("Академическая")
v81 = Station("Профсоюзная")
v82 = Station("Новые черемушки")
v83 = Station("Калужская")
v84 = Station("Беляево")
v85 = Station("Коньково")
v86 = Station("Теплый стан")
v87 = Station("Ясенево")
v88 = Station("Битцевский парк")

# красная ветка:
v89 = Station("Улица Подбельского")
v90 = Station("Черкизовская")
v91 = Station("Преображенская площадь")
v92 = Station("Сокольники")
v93 = Station("Красносельская")
v94 = Station("Комсомольская (радиальная)")
v95 = Station("Красные ворота")
v96 = Station("Чистые пруды")
v97 = Station("Лубянка")
v98 = Station("Охотный ряд")
v99 = Station("Библиотека имени Ленина")
v100 = Station("Кропоткинская")
v101 = Station("Парк культуры (радиальная)")
v102 = Station("Фрунзенская")
v103 = Station("Спортивная")
v104 = Station("Воробьевы горы")
v105 = Station("Университет")
v106 = Station("Проспект Вернадского")
v107 = Station("Юго-западная")

# синяя ветка:
v108 = Station("Щелковская")
v109 = Station("Первомайская")
v110 = Station("Измайловская")
v111 = Station("Измайловский парк")
v112 = Station("Семеновская")
v113 = Station("Электрозаводская")
v114 = Station("Бауманская")
v115 = Station("Курская (Радиальная)")
v116 = Station("Площадь революции")
v117 = Station("Арбатская (синяя)")
v118 = Station("Смоленская")
v119 = Station("Киевская (синяя)")

# желтая ветка:
v120 = Station("Новогиреево")
v121 = Station("Перово")
v122 = Station("Шоссе энтузиастов")
v123 = Station("Авиамоторная")
v124 = Station("Площадь Ильича")
v125 = Station("Марксисткая")
v126 = Station("Третьяковская (желтая)")

# cветло-зеленая ветка:
v127 = Station("Чкаловская")
v128 = Station("Римская")
v129 = Station("Крестьянская застава")
v130 = Station("Дубровка")
v131 = Station("Кожуховская")
v132 = Station("Печатники")
v133 = Station("Волжская")
v134 = Station("Люблино")
v135 = Station("Братиславская")
v136 = Station("Марьино")

# бирюзовая ветка:
v137 = Station("Каховская")
v138 = Station("Варшавская")
v139 = Station("Каширская (бирюзовая)")

# голубая ветка:
v140 = Station("Крылатская")
v141 = Station("Молодежная")
v142 = Station("Кунцевская")
v143 = Station("Пионерская")
v144 = Station("Филевский парк")
v145 = Station("Багратионовская")
v146 = Station("Фили")
v147 = Station("Кутузовская")
v148 = Station("Студенческая")
v149 = Station("Киевская (голубая)")
v150 = Station("Смоленская")
v151 = Station("Арбатская (голубая)")
v152 = Station("Александровский сад")

# кольцо:
v153 = Station("Новослободская (кольцевая)")
v154 = Station("Менделеевская")
v155 = Station("Комсомольская (кольцевая)")
v156 = Station("Курская (кольцевая)")
v157 = Station("Таганская (кольцевая)")
v158 = Station("Павелецкая (кольцевая)")
v159 = Station("Добрынинская")
v160 = Station("Октябрьская (кольцевая)")
v161 = Station("Парк-культуры (кольцевая)")
v162 = Station("Киевская (кольцевая)")
v163 = Station("Краснопресненская")
v164 = Station("Белорусская (кольцевая)")

# Перегоны
# кольцо перегоны
map_metro.add_link(LinkMetro(v153, v154, 3))
map_metro.add_link(LinkMetro(v154, v155, 2))
map_metro.add_link(LinkMetro(v155, v156, 3))
map_metro.add_link(LinkMetro(v156, v157, 2))
map_metro.add_link(LinkMetro(v157, v158, 2))
map_metro.add_link(LinkMetro(v158, v159, 2))
map_metro.add_link(LinkMetro(v159, v160, 2))
map_metro.add_link(LinkMetro(v160, v161, 2))
map_metro.add_link(LinkMetro(v161, v162, 3))
map_metro.add_link(LinkMetro(v162, v163, 3))
map_metro.add_link(LinkMetro(v163, v164, 3))
map_metro.add_link(LinkMetro(v164, v153, 2))

# голубой перегоны
map_metro.add_link(LinkMetro(v140, v141, 3))
map_metro.add_link(LinkMetro(v141, v142, 3))
map_metro.add_link(LinkMetro(v142, v143, 2))
map_metro.add_link(LinkMetro(v143, v144, 2))
map_metro.add_link(LinkMetro(v144, v145, 2))
map_metro.add_link(LinkMetro(v145, v146, 2))
map_metro.add_link(LinkMetro(v146, v147, 3))
map_metro.add_link(LinkMetro(v147, v148, 2))
map_metro.add_link(LinkMetro(v148, v149, 2))
map_metro.add_link(LinkMetro(v149, v150, 3))
map_metro.add_link(LinkMetro(v150, v151, 2))
map_metro.add_link(LinkMetro(v151, v152, 1))

# бирюзовый перегоны
map_metro.add_link(LinkMetro(v137, v138, 2))
map_metro.add_link(LinkMetro(v138, v139, 2))

# светло-зеленый перегоны
map_metro.add_link(LinkMetro(v127, v128, 3))
map_metro.add_link(LinkMetro(v128, v129, 3))
map_metro.add_link(LinkMetro(v129, v130, 2))
map_metro.add_link(LinkMetro(v130, v131, 2))
map_metro.add_link(LinkMetro(v131, v132, 4))
map_metro.add_link(LinkMetro(v132, v133, 2))
map_metro.add_link(LinkMetro(v133, v134, 3))
map_metro.add_link(LinkMetro(v134, v135, 3))
map_metro.add_link(LinkMetro(v135, v136, 2))

# желтый перегоны
map_metro.add_link(LinkMetro(v120, v121, 3))
map_metro.add_link(LinkMetro(v121, v122, 3))
map_metro.add_link(LinkMetro(v122, v123, 3))
map_metro.add_link(LinkMetro(v123, v124, 3))
map_metro.add_link(LinkMetro(v124, v125, 3))
map_metro.add_link(LinkMetro(v125, v126, 2))

# синий перегоны
map_metro.add_link(LinkMetro(v108, v109, 2))
map_metro.add_link(LinkMetro(v109, v110, 3))
map_metro.add_link(LinkMetro(v110, v111, 4))
map_metro.add_link(LinkMetro(v111, v112, 2))
map_metro.add_link(LinkMetro(v112, v113, 2))
map_metro.add_link(LinkMetro(v113, v114, 2))
map_metro.add_link(LinkMetro(v114, v115, 3))
map_metro.add_link(LinkMetro(v115, v116, 4))
map_metro.add_link(LinkMetro(v116, v117, 2))
map_metro.add_link(LinkMetro(v117, v118, 3))
map_metro.add_link(LinkMetro(v118, v119, 2))

# красный перегоны
map_metro.add_link(LinkMetro(v89, v90, 3))
map_metro.add_link(LinkMetro(v90, v91, 3))
map_metro.add_link(LinkMetro(v91, v92, 3))
map_metro.add_link(LinkMetro(v92, v93, 1))
map_metro.add_link(LinkMetro(v93, v94, 1))
map_metro.add_link(LinkMetro(v94, v95, 2))
map_metro.add_link(LinkMetro(v95, v96, 1))
map_metro.add_link(LinkMetro(v96, v97, 1))
map_metro.add_link(LinkMetro(v97, v98, 1))
map_metro.add_link(LinkMetro(v98, v99, 1))
map_metro.add_link(LinkMetro(v99, v100, 2))
map_metro.add_link(LinkMetro(v100, v101, 2))
map_metro.add_link(LinkMetro(v101, v102, 3))
map_metro.add_link(LinkMetro(v102, v103, 1))
map_metro.add_link(LinkMetro(v103, v104, 3))
map_metro.add_link(LinkMetro(v104, v105, 3))
map_metro.add_link(LinkMetro(v105, v106, 2))
map_metro.add_link(LinkMetro(v106, v107, 3))

# оранжевый перегоны
map_metro.add_link(LinkMetro(v65, v66, 3))
map_metro.add_link(LinkMetro(v66, v67, 3))
map_metro.add_link(LinkMetro(v67, v68, 2))
map_metro.add_link(LinkMetro(v68, v69, 4))
map_metro.add_link(LinkMetro(v69, v70, 2))
map_metro.add_link(LinkMetro(v70, v71, 3))
map_metro.add_link(LinkMetro(v71, v72, 2))
map_metro.add_link(LinkMetro(v72, v73, 2))
map_metro.add_link(LinkMetro(v73, v74, 2))
map_metro.add_link(LinkMetro(v74, v75, 2))
map_metro.add_link(LinkMetro(v75, v76, 3))
map_metro.add_link(LinkMetro(v76, v77, 3))
map_metro.add_link(LinkMetro(v77, v78, 2))
map_metro.add_link(LinkMetro(v78, v79, 3))
map_metro.add_link(LinkMetro(v79, v80, 3))
map_metro.add_link(LinkMetro(v80, v81, 3))
map_metro.add_link(LinkMetro(v81, v82, 2))
map_metro.add_link(LinkMetro(v82, v83, 2))
map_metro.add_link(LinkMetro(v83, v84, 3))
map_metro.add_link(LinkMetro(v84, v85, 2))
map_metro.add_link(LinkMetro(v85, v86, 3))
map_metro.add_link(LinkMetro(v86, v87, 3))
map_metro.add_link(LinkMetro(v87, v88, 2))

# серый перегоны
map_metro.add_link(LinkMetro(v40, v41, 3))
map_metro.add_link(LinkMetro(v41, v42, 3))
map_metro.add_link(LinkMetro(v42, v43, 3))
map_metro.add_link(LinkMetro(v43, v44, 3))
map_metro.add_link(LinkMetro(v44, v45, 2))
map_metro.add_link(LinkMetro(v45, v46, 2))
map_metro.add_link(LinkMetro(v46, v47, 3))
map_metro.add_link(LinkMetro(v47, v48, 2))
map_metro.add_link(LinkMetro(v48, v49, 2))
map_metro.add_link(LinkMetro(v49, v50, 2))
map_metro.add_link(LinkMetro(v50, v51, 2))
map_metro.add_link(LinkMetro(v51, v52, 3))
map_metro.add_link(LinkMetro(v52, v53, 2))
map_metro.add_link(LinkMetro(v53, v54, 3))
map_metro.add_link(LinkMetro(v54, v55, 3))
map_metro.add_link(LinkMetro(v55, v56, 2))
map_metro.add_link(LinkMetro(v56, v57, 2))
map_metro.add_link(LinkMetro(v57, v58, 2))
map_metro.add_link(LinkMetro(v58, v59, 3))
map_metro.add_link(LinkMetro(v59, v60, 3))
map_metro.add_link(LinkMetro(v60, v61, 2))
map_metro.add_link(LinkMetro(v61, v62, 2))
map_metro.add_link(LinkMetro(v62, v63, 2))
map_metro.add_link(LinkMetro(v63, v64, 3))

# зеленые перегоны
map_metro.add_link(LinkMetro(v20, v21, 3))
map_metro.add_link(LinkMetro(v21, v22, 3))
map_metro.add_link(LinkMetro(v22, v23, 3))
map_metro.add_link(LinkMetro(v23, v24, 2))
map_metro.add_link(LinkMetro(v24, v25, 3))
map_metro.add_link(LinkMetro(v25, v26, 2))
map_metro.add_link(LinkMetro(v26, v39, 2))
map_metro.add_link(LinkMetro(v39, v27, 1))
map_metro.add_link(LinkMetro(v27, v28, 2))
map_metro.add_link(LinkMetro(v28, v29, 3))
map_metro.add_link(LinkMetro(v29, v30, 3))
map_metro.add_link(LinkMetro(v30, v31, 4))
map_metro.add_link(LinkMetro(v31, v32, 5))
map_metro.add_link(LinkMetro(v32, v33, 4))
map_metro.add_link(LinkMetro(v33, v34, 4))
map_metro.add_link(LinkMetro(v34, v35, 3))
map_metro.add_link(LinkMetro(v35, v36, 4))
map_metro.add_link(LinkMetro(v36, v37, 2))
map_metro.add_link(LinkMetro(v37, v38, 2))

# фиолетовые перегоны
map_metro.add_link(LinkMetro(v1, v2, 3))
map_metro.add_link(LinkMetro(v2, v3, 3))
map_metro.add_link(LinkMetro(v3, v4, 4))
map_metro.add_link(LinkMetro(v4, v5, 2))
map_metro.add_link(LinkMetro(v5, v6, 3))
map_metro.add_link(LinkMetro(v6, v7, 2))
map_metro.add_link(LinkMetro(v7, v8, 2))
map_metro.add_link(LinkMetro(v8, v9, 2))
map_metro.add_link(LinkMetro(v9, v10, 3))
map_metro.add_link(LinkMetro(v10, v11, 2))
map_metro.add_link(LinkMetro(v11, v12, 2))
map_metro.add_link(LinkMetro(v12, v13, 3))
map_metro.add_link(LinkMetro(v13, v14, 3))
map_metro.add_link(LinkMetro(v14, v15, 2))
map_metro.add_link(LinkMetro(v15, v16, 4))
map_metro.add_link(LinkMetro(v16, v17, 2))
map_metro.add_link(LinkMetro(v17, v18, 3))
map_metro.add_link(LinkMetro(v18, v19, 3))

# Пересадки
# Кольцо
map_metro.add_link(TransferStation(v9, v163, 3))
map_metro.add_link(TransferStation(v26, v164, 3))
map_metro.add_link(TransferStation(v153, v48, 3))
map_metro.add_link(TransferStation(v72, v154, 3))
map_metro.add_link(TransferStation(v94, v155, 3))
map_metro.add_link(TransferStation(v115, v156, 3))
map_metro.add_link(TransferStation(v115, v127, 3))
map_metro.add_link(TransferStation(v156, v127, 3))
map_metro.add_link(TransferStation(v125, v157, 3))
map_metro.add_link(TransferStation(v157, v13, 3))
map_metro.add_link(TransferStation(v125, v13, 3))
map_metro.add_link(TransferStation(v158, v30, 4))
map_metro.add_link(TransferStation(v159, v53, 3))
map_metro.add_link(TransferStation(v77, v160, 2))
map_metro.add_link(TransferStation(v101, v161, 2))
map_metro.add_link(TransferStation(v162, v119, 2))
map_metro.add_link(TransferStation(v162, v149, 4))
map_metro.add_link(TransferStation(v119, v149, 4))

# Внутри кольца
map_metro.add_link(TransferStation(v117, v152, 3))
map_metro.add_link(TransferStation(v117, v51, 2))
map_metro.add_link(TransferStation(v99, v51, 3))
map_metro.add_link(TransferStation(v99, v152, 3))
map_metro.add_link(TransferStation(v99, v117, 3))
map_metro.add_link(TransferStation(v50, v10, 3))
map_metro.add_link(TransferStation(v27, v10, 3))
map_metro.add_link(TransferStation(v27, v50, 4))
map_metro.add_link(TransferStation(v97, v11, 2))
map_metro.add_link(TransferStation(v116, v28, 3))
map_metro.add_link(TransferStation(v98, v28, 3))
map_metro.add_link(TransferStation(v76, v126, 1))
map_metro.add_link(TransferStation(v29, v126, 4))
map_metro.add_link(TransferStation(v29, v76, 4))
map_metro.add_link(TransferStation(v12, v75, 1.5))
map_metro.add_link(TransferStation(v96, v74, 2))

# Снаружи кольца
map_metro.add_link(TransferStation(v124, v128, 2))
map_metro.add_link(TransferStation(v129, v14, 3))
map_metro.add_link(TransferStation(v139, v33, 2))
map_metro.add_link(TransferStation(v137, v58, 2))
map_metro.add_link(TransferStation(v137, v58, 2))


print(len(map_metro._links))
print(len(map_metro._nodes))
path = map_metro.find_path(v137, v58)

print(path)
