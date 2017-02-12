import os
import sqlite3 as sql
from DivvyStationsRun import divvy_create_graph

cd = os.path.dirname(os.path.abspath(__file__))

try:
    conn = sql.connect(os.path.join(cd, "Divvy_Trips.db"))
    sql = "SELECT DISTINCT [FROM STATION ID], [FROM STATION NAME] FROM trips;"

    cur = conn.cursor()
    cur.execute(sql)
    stations = cur.fetchall()
    cur.close()
    conn.close()
    
    for s in stations:
        print(s[0], s[1])
        divvy_create_graph(s[0], s[1])

except Exception as e:
    print(e)
    
finally:
    print("Successfully completed!")

""" STATIONS
502 California Ave & Altgeld St
195 Columbus Dr & Randolph St
199 Wabash Ave & Grand Ave
47 State St & Kinzie St
177 Theater on the Lake
264 Stetson Ave & South Water St
77 Clinton St & Madison St
15 Racine Ave & 18th St
427 Cottage Grove Ave & 63rd St
405 Wentworth Ave & 35th St
256 Broadway & Sheridan Rd
239 Western Ave & Leland Ave
175 Wells St & Polk St
130 Damen Ave & Division St
267 Lake Park Ave & 47th St
88 May St & Randolph St
59 Wabash Ave & Roosevelt Rd
55 Halsted St & Roosevelt Rd
346 Ada St & Washington Blvd
300 Broadway & Barry Ave
343 Racine Ave & Wrightwood Ave
295 Broadway & Argyle St
67 Sheffield Ave & Fullerton Ave
134 Peoria St & Jackson Blvd
22 May St & Taylor St
72 Wabash Ave & 16th St
60 Dayton St & North Ave
26 McClurg Ct & Illinois St
143 Sedgwick St & Webster Ave
120 Wentworth Ave & Archer Ave
308 Seeley Ave & Roscoe St
144 Larrabee St & Webster Ave
52 Michigan Ave & Lake St
340 Clark St & Wrightwood Ave
142 McClurg Ct & Erie St
299 Halsted St & Roscoe St
418 Ellis Ave & 53rd St
76 Lake Shore Dr & Monroe St
243 Lincoln Ave & Leavitt St
305 Western Ave & Division St
49 Dearborn St & Monroe St
482 Campbell Ave & Montrose Ave
127 Lincoln Ave & Fullerton Ave
279 Halsted St & 35th St (*)
342 Wolcott Ave & Polk St
41 Federal St & Polk St
186 Ogden Ave & Race Ave
210 Ashland Ave & Division St
205 Paulina St & 18th St
290 Kedzie Ave & Palmer Ct
463 Clark St & Berwyn Ave
464 Damen Ave & Foster Ave
61 Wood St & Milwaukee Ave
24 Fairbanks Ct & Grand Ave
434 Ogden Ave & Roosevelt Rd
451 Sheridan Rd & Loyola Ave
145 Mies van der Rohe Way & Chestnut St
467 Western Ave & Lunt Ave
158 Milwaukee Ave & Wabansia Ave
92 Carpenter St & Huron St
349 Halsted St & Wrightwood Ave
111 Sedgwick St & Huron St
17 Wood St & Division St
126 Clark St & North Ave
294 Broadway & Berwyn Ave
118 Sedgwick St & North Ave
275 Ashland Ave & 13th St
112 Green St & Randolph St
320 Loomis St & Lexington St
141 Clark St & Lincoln Ave
53 Wells St & Huron St
274 Racine Ave & 15th St
261 Hermitage Ave & Polk St
244 Ravenswood Ave & Irving Park Rd
74 Kingsbury St & Erie St
156 Clark St & Wellington Ave
333 Ashland Ave & Blackhawk St
211 St. Clair St & Erie St
29 Noble St & Milwaukee Ave
298 Lincoln Ave & Belle Plaine Ave
458 Broadway & Thorndale Ave
165 Clark St & Grace St
286 Franklin St & Quincy St
117 Wilton Ave & Belmont Ave
38 Clark St & Lake St
488 Pulaski Rd & Eddy St
58 Marshfield Ave & Cortland St
214 Damen Ave & Grand Ave
43 Michigan Ave & Washington St
331 Halsted St & Blackhawk St (*)
226 Racine Ave & Belmont Ave
183 Damen Ave & Augusta Blvd
93 Sheffield Ave & Willow St
94 Clark St & Armitage Ave
138 Clybourn Ave & Division St
306 Sheridan Rd & Buena Ave
18 Wacker Dr & Washington St
110 Dearborn St & Erie St
240 Sheridan Rd & Irving Park Rd
297 Paulina St & Montrose Ave
220 Hampden Ct & Diversey Pkwy
44 State St & Randolph St
510 Spaulding Ave & Division St
99 Lake Shore Dr & Ohio St
197 Michigan Ave & Madison St
313 Lakeview Ave & Fullerton Pkwy
30 Ashland Ave & Augusta Blvd
254 Pine Grove Ave & Irving Park Rd
314 Ravenswood Ave & Berteau Ave
194 Wabash Ave & Wacker Pl
212 Orleans St & Ohio St
27 Larrabee St & North Ave
602 Central St & Girard Ave
312 Clarendon Ave & Gordon Ter
234 Clark St & Montrose Ave
276 California Ave & North Ave
315 Elston Ave & Wabansia Ave
159 Claremont Ave & Hirsch St
477 Manor Ave & Leland Ave
394 Clark St & 9th St (AMLI)
503 Drake Ave & Fullerton Ave
475 Washtenaw Ave & Lawrence Ave
190 Southport Ave & Wrightwood Ave
615 Lombard Ave & Madison St
250 Ashland Ave & Wellington Ave
96 Desplaines St & Randolph St
106 State St & Pearson St
304 Broadway & Waveland Ave
459 Lakefront Trail & Bryn Mawr Ave
133 Kingsbury St & Kinzie St
316 Damen Ave & Sunnyside Ave
478 Rockwell St & Eastwood Ave
182 Wells St & Elm St
233 Sangamon St & Washington Blvd (*)
325 Clark St & Winnemac Ave
480 Albany (Kedzie) Ave & Montrose Ave
382 Western Ave & Congress Pkwy
338 Calumet Ave & 18th St
128 Damen Ave & Chicago Ave
227 Southport Ave & Waveland Ave
161 Rush St & Superior St
176 Clark St & Elm St
90 Millennium Park
289 Wells St & Concord Ln
46 Wells St & Walton St
170 Clinton St & 18th St
414 Canal St & Taylor St
14 Morgan St & 18th St
413 Woodlawn Ave & Lake Park Ave
283 LaSalle St & Jackson Blvd
160 Campbell Ave & North Ave
253 Clifton Ave & Lawrence Ave
303 Broadway & Cornelia Ave
426 Ellis Ave & 60th St
447 Glenwood Ave & Morse Ave
359 Larrabee St & Division St
19 Loomis St & Taylor St (*)
80 Aberdeen St & Monroe St
108 Halsted St & Polk St
259 California Ave & Francis Pl
3 Shedd Aquarium
6 Dusable Harbor
109 900 W Harrison St
454 Broadway & Granville Ave
219 Damen Ave & Cortland St
296 Broadway & Belmont Ave
51 Clark St & Randolph St
35 Streeter Dr & Grand Ave
280 Morgan St & 31st St
415 Calumet Ave & 51st St
4 Burnham Harbor
486 Oakley Ave & Irving Park Rd
157 Lake Shore Dr & Wellington Ave
89 Financial Pl & Congress Pkwy
374 Western Ave & Walton St
344 Ravenswood Ave & Lawrence Ave
231 Sheridan Rd & Montrose Ave
432 Clark St & Lunt Ave
507 Humboldt Blvd & Armitage Ave
302 Sheffield Ave & Wrightwood Ave
273 Michigan Ave & 18th St
115 Sheffield Ave & Wellington Ave
16 Paulina Ave & North Ave
97 Field Museum
260 Kedzie Ave & Milwaukee Ave
520 Greenview Ave & Jarvis Ave
293 Broadway & Wilson Ave
255 Indiana Ave & Roosevelt Rd
129 Blue Island Ave & 18th St
493 Western Ave & Roscoe St
291 Wells St & Evergreen Ave
341 Adler Planetarium
166 Ashland Ave & Wrightwood Ave
31 Franklin St & Chicago Ave
229 Southport Ave & Roscoe St
284 Michigan Ave & Jackson Blvd
56 Desplaines St & Kinzie St
48 Larrabee St & Kingsbury St
172 Rush St & Cedar St
84 Union Ave & Grand Ave
327 Sheffield Ave & Webster Ave
232 Pine Grove Ave & Waveland Ave
69 Damen Ave & Pierce Ave
433 Kedzie Ave & Harrison St
248 Woodlawn Ave & 55th St
282 Halsted St & Maxwell St
401 Shields Ave & 28th Pl
73 Jefferson St & Monroe St
174 Canal St & Madison St
181 LaSalle St & Illinois St
213 Leavitt St & North Ave
251 Clarendon Ave & Leland Ave
131 Lincoln Ave & Belmont Ave
5 State St & Harrison St
21 Aberdeen St & Jackson Blvd
100 Orleans St & Merchandise Mart Plaza
373 Kedzie Ave & Chicago Ave
209 Normal Ave & Archer Ave
39 Wabash Ave & Adams St
237 MLK Jr Dr & 29th St
465 Marine Dr & Ainslie St
461 Broadway & Ridge Ave
288 Larrabee St & Armitage Ave
332 Halsted St & Diversey Pkwy
191 Canal St & Monroe St (*)
550 Central Ave & Chicago Ave
37 Dearborn St & Adams St
544 Mason Ave & Madison St
258 Logan Blvd & Elston Ave
57 Clinton St & Roosevelt Rd
20 Sheffield Ave & Kingsbury St
116 Western Ave & Winnebago Ave
2 Michigan Ave & Balbo Ave
45 Michigan Ave & Congress Pkwy
523 Eastlake Ter & Rogers Ave
607 Cuyler Ave & Augusta St
28 Larrabee St & Menomonee St
87 Racine Ave & Fullerton Ave
366 Loomis St & Archer Ave
33 State St & Van Buren St
268 Lake Shore Dr & North Blvd
481 California Ave & Montrose Ave
257 Lincoln Ave & Waveland Ave
301 Clark St & Schiller St
324 Stockton Dr & Wrightwood Ave
249 Montrose Harbor
491 Talman Ave & Addison St
285 Wood St & Hubbard St
7 Field Blvd & South Water St
123 California Ave & Milwaukee Ave
309 Leavitt St & Armitage Ave
121 Blackstone Ave & Hyde Park Blvd
334 Lake Shore Dr & Belmont Ave
420 Ellis Ave & 55th St
85 Michigan Ave & Oak St
424 Museum of Science and Industry
419 Lake Park Ave & 53rd St
119 Ashland Ave & Lake St
198 Green St & Madison St
435 Kedzie Ave & Roosevelt Rd
113 Bissell St & Armitage Ave
150 Fort Dearborn Dr & 31st St
13 Wilton Ave & Diversey Pkwy
217 May St & Fulton St
66 Clinton St & Lake St
430 MLK Jr Dr & 63rd St
225 Halsted St & Dickens Ave
153 Southport Ave & Wellington Ave
91 Clinton St & Washington Blvd
271 Cottage Grove Ave & 43rd St
71 Morgan St & Lake St
383 Ashland Ave & Harrison St
247 Shore Dr & 55th St
242 Damen Ave & Leland Ave
81 Daley Center Plaza
114 Sheffield Ave & Waveland Ave
216 California Ave & Division St
489 Drake Ave & Addison St
122 Ogden Ave & Congress Pkwy
238 Ravenswood Ave & Montrose Ave (*)
137 Morgan Ave & 14th Pl
40 LaSalle St & Adams St
402 Shields Ave & 31st St
50 Clark St & Congress Pkwy
345 Lake Park Ave & 56th St
107 Desplaines St & Jackson Blvd
152 Lincoln Ave & Diversey Pkwy
501 Richmond St & Diversey Ave
36 Franklin St & Jackson Blvd
25 Michigan Ave & Pearson St
455 Maplewood Ave & Peterson Ave
329 Lake Shore Dr & Diversey Pkwy
307 Southport Ave & Clybourn Ave
140 Dearborn Pkwy & Delaware Pl
351 Cottage Grove Ave & 51st St
277 Ashland Ave & Grand Ave
188 Greenview Ave & Fullerton Ave
490 Troy St & Elston Ave
321 Wabash Ave & 8th St
245 Clarendon Ave & Junior Ter
154 Southport Ave & Belmont Ave
192 Canal St & Adams St
509 Troy St & North Ave
32 Racine Ave & Congress Pkwy
241 Morgan St & Polk St
336 Cottage Grove Ave & 47th St
224 Halsted St & Willow St
504 Campbell Ave & Fullerton Ave
350 Ashland Ave & Chicago Ave
163 Damen Ave & Clybourn Ave
605 University Library (NU)
164 Franklin St & Lake St
527 Western Ave & Howard St
173 Mies van der Rohe Way & Chicago Ave
411 Halsted St & 47th Pl
168 Michigan Ave & 14th St
347 Ashland Ave & Grace St
364 Larrabee St & Oak St
230 Lincoln Ave & Roscoe St
524 Austin Blvd & Chicago Ave
310 Damen Ave & Charleston St
460 Clark St & Bryn Mawr Ave
532 Austin Blvd & Lake St
547 Ashland Ave & Pershing Rd
328 Ellis Ave & 58th St
318 Southport Ave & Irving Park Rd
376 Artesian Ave & Hubbard St
337 Clark St & Chicago Ave
323 Sheridan Rd & Lawrence Ave
515 Paulina St & Howard St
317 Wood St & Taylor St
223 Clifton Ave & Armitage Ave
162 Damen Ave & Wellington Ave
479 Drake Ave & Montrose Ave
103 Clinton St & Polk St (*)
322 Kimbark Ave & 53rd St
339 Emerald Ave & 31st St
499 Kosciuszko Park
596 Benson Ave & Church St
180 Ritchie Ct & Banks St
34 Cannon Dr & Fullerton Ave
86 Eckhart Park
476 Kedzie Ave & Leland Ave
326 Clark St & Leland Ave
68 Clinton St & Tilden St
417 Cornell Ave & Hyde Park Blvd
367 Racine Ave & 35th St
609 Forest Ave & Lake St
23 Orleans St & Elm St (*)
620 Orleans St & Chestnut St (NEXT Apts)
246 Ashland Ave & Belle Plaine Ave
124 Damen Ave & Cullerton St
42 Wabash Ave & Cermak Rd
228 Damen Ave & Melrose Ave
518 Conservatory Dr & Lake St
75 Clinton St & Jackson Blvd
54 Ogden Ave & Chicago Ave
319 Greenview Ave & Diversey Pkwy
203 Western Ave & 21st St
603 Chicago Ave & Sheridan Rd
132 Wentworth Ave & 24th St
604 Sheridan Rd & Noyes St (NU)
202 Halsted St & 18th St
472 Lincoln Ave & Winona St
526 Oakley Ave & Touhy Ave
378 California Ave & Lake St
196 Cityfront Plaza Dr & Pioneer Ct
598 Elmwood Ave & Austin St
597 Chicago Ave & Washington St
125 Rush St & Hubbard St
311 Leavitt St & Lawrence Ave
453 Clark St & Schreiber Ave
457 Clark St & Elmdale Ave
178 State St & 19th St
590 Kilbourn Ave & Irving Park Rd
98 LaSalle St & Washington St
487 California Ave & Byron St
471 Francisco Ave & Foster Ave
265 Cottage Grove Ave & Oakwood Blvd
462 Ravenswood Ave & Balmoral Ave
272 Indiana Ave & 31st St
595 Wabash Ave & 87th St
429 Cottage Grove Ave & 67th St
619 Keystone Ave & Fullerton Ave
169 Canal St & Harrison St
287 Franklin St & Monroe St
215 Damen Ave & Madison St
167 Damen Ave & Coulter St
423 University Ave & 57th St
222 Milwaukee Ave & Rockwell St
185 Stave St & Armitage Ave
278 Wallace St & 35th St
517 Clark St & Jarvis Ave
135 Halsted St & 21st St
292 Southport Ave & Clark St
612 Ridgeland Ave & Lake St
511 Albany Ave & Bloomingdale Ave
403 Wentworth Ave & 33rd St
545 Kostner Ave & Adams St
201 Indiana Ave & 40th St
149 Calumet Ave & 33rd St
474 Christiana Ave & Lawrence Ave
514 Ridge Blvd & Howard St
611 Oak Park Ave & South Blvd
591 Kilbourn Ave & Milwaukee Ave
600 Dodge Ave & Church St
496 Avers Ave & Belmont Ave
610 Marion St & South Blvd
497 Kimball Ave & Belmont Ave
601 Central St Metra
397 Saginaw Ave & Exchange Ave
399 South Shore Dr & 74th St
377 Kedzie Ave & Lake St
148 State St & 33rd St
370 Calumet Ave & 21st St
136 Racine Ave & 13th St
505 Winchester Ave & Elston Ave
428 Dorchester Ave & 63rd St
365 Halsted St & North Branch St
263 Rhodes Ave & 32nd St
437 Washtenaw Ave & 15th St (*)
422 DuSable Museum
506 Spaulding Ave & Armitage Ave
354 Sheridan Rd & Greenleaf Ave
442 California Ave & 23rd Pl
449 Clark St & Columbia Ave
483 Avondale Ave & Irving Park Rd
606 Forest Ave & Chicago Ave
236 Sedgwick St & Schiller St
425 Harper Ave & 59th St
146 Loomis St & Jackson Blvd
184 State St & 35th St
356 Stony Island Ave & 71st St
204 Prairie Ave & Garfield Blvd
577 Stony Island Ave & South Chicago Ave
147 Indiana Ave & 26th St
206 Halsted St & Archer Ave
519 Wolcott Ave & Fargo Ave
525 Glenwood Ave & Touhy Ave
390 Wentworth Ave & 63rd St
500 Central Park Ave & Elbridge Ave
438 Central Park Ave & Ogden Ave
441 Kedzie Ave & 24th St
208 Ashland Ave & 21st St
552 Ashland Ave & McDowell Ave
62 McCormick Place
330 Lincoln Ave & Addison St
485 Sawyer Ave & Irving Park Rd
372 Humboldt Dr & Luis Munoz Marin Dr
368 Ashland Ave & Archer Ave
616 Oak Park Ave & Harrison St
200 MLK Jr Dr & 47th St
171 May St & Cullerton St
207 Emerald Ave & 28th St
613 Wisconsin Ave & Madison St
9 Leavitt St & Archer Ave
11 Jeffery Blvd & 71st St
352 Jeffery Blvd & 67th St
431 Eberhart Ave & 61st St
270 Stony Island Ave & 75th St
218 Wells St & 19th St
395 Jeffery Blvd & 76th St
95 Stony Island Ave & 64th St
421 MLK Jr Dr & 56th St (*)
439 Kedzie Ave & 21st St
470 Kedzie Ave & Foster Ave
469 St. Louis Ave & Balmoral Ave
436 Fairfield Ave & Roosevelt Rd
385 Princeton Ave & Garfield Blvd
492 Leavitt St & Addison St
508 Central Park Ave & North Ave
498 California Ave & Fletcher St
581 Commercial Ave & 83rd St
408 Union Ave & 42nd St
617 East Ave & Garfield St
468 Budlong Woods Library
444 Albany Ave & 26th St
416 Dorchester Ave & 49th St
443 Millard Ave & 26th St
522 Bosworth Ave & Howard St
281 Western Ave & 24th St
448 Warren Park East
335 Calumet Ave & 35th St
589 Milwaukee Ave & Cuyler Ave
12 South Shore Dr & 71st St
554 Damen Ave & 51st St
348 California Ave & 21st St
599 Valli Produce - Evanston Plaza
494 Kedzie Ave & Bryn Mawr Ave
101 63rd St Beach
614 East Ave & Madison St
355 South Shore Dr & 67th St
252 Greenwood Ave & 47th St
381 Western Ave & Monroe St
495 Keystone Ave & Montrose Ave
466 Ridge Blvd & Touhy Ave
452 Western Ave & Granville Ave
102 Stony Island Ave & 67th St
406 Lake Park Ave & 35th St
585 Cottage Grove Ave & 83rd St
375 Sacramento Blvd & Franklin Blvd
410 Prairie Ave & 43rd St
193 State St & 29th St
484 Monticello Ave & Irving Park Rd
400 Cottage Grove Ave & 71st St
618 Lombard Ave & Garfield St
440 Lawndale Ave & 23rd St
528 Pulaski Rd & Lake St
384 Halsted St & 51st St
369 Wood St & 35th St
592 Knox Ave & Montrose Ave
594 Western Blvd & 48th Pl
412 Princeton Ave & 47th St
445 California Ave & 26th St
456 2112 W Peterson Ave
546 Damen Ave & Pershing Rd
551 Hoyne Ave & 47th St
262 Halsted St & 37th St
535 Pulaski Rd & Congress Pkwy
353 Clark St & Touhy Ave
179 MLK Jr Dr & Oakwood Blvd
392 Perry Ave & 69th St
450 Warren Park West
560 Marshfield Ave & 59th St
608 Humphrey Ave & Ontario St
540 Laramie Ave & Madison St
542 Central Ave & Madison St
543 Laramie Ave & Gladys Ave
583 Stony Island Ave & 82nd St
393 Calumet Ave & 71st St
446 Western Ave & 28th St
407 State St & Pershing Rd
548 Morgan St & Pershing Rd
567 May St & 69th St
531 Central Ave & Lake St
559 Racine Ave & Garfield Blvd
388 Halsted St & 63rd St
563 Ashland Ave & 63rd St
536 Kostner Ave & Lake St
537 Kenton Ave & Madison St
386 Halsted St & 56th St
576 Greenwood Ave & 79th St
534 Pulaski Rd & Madison St
578 Chappel Ave & 79th St
574 Vernon Ave & 79th St
533 Central Park Blvd & 5th Ave
564 Racine Ave & 65th St
584 Ellis Ave & 83rd St
573 State St & 79th St
568 Normal Ave & 72nd St
553 Elizabeth St & 47th St
572 State St & 76th St
409 Shields Ave & 43rd St
587 Wabash Ave & 83rd St
565 Ashland Ave & 66th St
391 Halsted St & 69th St
571 Vernon Ave & 75th St
593 Halsted St & 59th St
579 Phillips Ave & 79th St
558 Ashland Ave & Garfield Blvd
580 Exchange Ave & 79th St
566 Ashland Ave & 69th St
541 Central Ave & Harrison St
555 Ashland Ave & 50th St
530 Laramie Ave & Kinzie St
575 Cottage Grove Ave & 78th St
538 Cicero Ave & Flournoy St
569 Woodlawn Ave & 75th St
398 Rainbow Beach
561 Damen Ave & 61st St
549 Marshfield Ave & 44th St
529 Cicero Ave & Lake St
586 MLK Jr Dr & 83rd St
539 Cicero Ave & Quincy St
556 Throop St & 52nd St
114 Sheffield Ave & Addison St
75 Canal St & Jackson Blvd
285 Wood St & Grand Ave
396 Yates Blvd & 75th St
588 South Chicago Ave & 83rd St
570 Evans Ave & 75th St
582 Phillips Ave & 82nd St
557 Damen Ave & Garfield Blvd
562 Racine Ave & 61st St
97 Museum Campus
480 Kedzie Ave & Montrose Ave
483 Keeler Ave & Irving Park Rd
35 Streeter Dr & Illinois St
19 Loomis St & Taylor St
331 Halsted St & Blackhawk St
289 Wells St & Concord Pl
279 Halsted St & 35th St
53 Wells St & Erie St
72 Wabash Ave (State St) & 16th St
80 Aberdeen St & Monroe St (Madison St)
198 Green St (Halsted St) & Madison St
103 Clinton St & Polk St
212 Wells St & Hubbard St
233 Sangamon St & Washington Blvd
191 Canal St & Monroe St
238 Ravenswood Ave & Montrose Ave
437 Washtenaw Ave & 15th St
16 Paulina  Ave (Wood St) & North Ave
247 Shore Drive & 55th St
23 Orleans St & Elm St
2 Buckingham Fountain
421 MLK Jr Dr & 56th St
402 Princeton Ave & 31st St
273 Michigan Ave & 16th St
80 Aberdeen St & Madison St
198 Halsted St & Madison St
287 Franklin St & Arcade Pl
72 State St & 16th St
55 Halsted St & James M Rochford St
16 Wood St & North Ave
417 Cornell Ave & Hyde Park B lvd
315 Leavitt St & Hirsch St
372 California Ave & Augusta Blvd
436 California Ave & Roosevelt Rd
414 Princeton Ave & China Pl
488 Pulaksi Rd & Eddy St
110 State St & Erie St
304 Halsted St & Waveland Ave
211 St Clair St & Erie St
15 Racine Ave & 19th St
109 900 W Harrison
278 Wallace Ave & 35th St
165 Clark St & Waveland Ave
237 Martin Luther King Dr & 29th St
196 Cityfront Plaza & N Water St
344 Wolcott Ave & Lawrence Ave
311 Lincoln Ave & Eastwood Ave
84 Green St & Milwaukee Ave
194 State St & Wacker Dr
200 King Dr & 47th St
163 Paulina St & Diversey Pkwy
179 Martin Luther King Dr & Oakwood Blvd
232 Pine Grove Ave & Addison St
122 Congress Pkwy & Ogden Ave
212 Wells St & Ohio St
58 Ashland Ave & Armitage Ave
94 Lincoln Ave & Armitage Ave
219 Damen Ave & Cortland Ave
"""
