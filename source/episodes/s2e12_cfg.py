import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E12_This_Christmas.pdf')
PARTS = [D + 's2e12_part1.txt', D + 's2e12_part2.txt', D + 's2e12_part3.txt']
EP = date(2005, 12, 22)
CODE = '2x12'
SEASON_LINE = 'Season 2, Episode 12'
TITLE = 'This Christmas'
COUNTERPART = "Episode 2x12. The counterpart of <i>Grey's Anatomy</i> 2x12 (the Christmas episode)."
DATES = 'Thursday, December 22, 2005 (day three of the TWU transit strike), 5:12 AM through 11:56 PM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x11'
AGES_ON = 'Thursday, December 22, 2005'

CAST = [
 ("Howard Divine", "Harmony's father; TWU Local 100 bus operator (on strike)", date(1950,8,30)), ("Lillian Divine", "Harmony's mother", date(1952,2,14)),
 ("Dr. Raven Ellison", "Surgical Intern", date(1979,12,3)), ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)),
 ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)), ("Dr. Bryce Kennerly", "Surgical Intern (on probation)", date(1978,6,11)),
 ("Dr. Elxa Bullock", "Surgical Resident (33 weeks pregnant)", date(1977,8,29)), ("Dr. Amond Baker", "Surgical Intern", date(1979,2,10)),
 ("Earl Peebles (new)", "Patient: 14-foot roof fall, splenic laceration", date(1947,11,30)), ("Dorothy Peebles (new)", "Earl's wife", date(1949,6,18)),
 ("Dr. Abraham Lowery", "Attending General Surgeon", date(1947,1,9)), ("Nurse Gloria Pettiford", "Head ER Nurse", date(1952,4,14)),
 ("Lady Bernadine Starks (new)", "Patient: bleeding duodenal ulcer, gospel recording artist", date(1956,3,8)), ("Freddie Lyle (new)", "Bernadine's manager", date(1953,7,7)),
 ("Brother Oliver Pettway (new)", "Bernadine's choir director", date(1961,10,2)), ("Yvonne Starks (new)", "Bernadine's sister", date(1960,4,11)),
 ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)), ("Kamari Fields (new)", "Patient: failing Fontan, heart transplant", date(1991,4,24)),
 ("Nadine Fields (new)", "Kamari's mother; MTA station agent (on strike)", date(1967,8,1)), ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)),
 ("Quentin Bascomb (new)", "Patient: cyclist, epidural hematoma", date(1974,1,29)), ("Dr. Arianna Cummings", "Surgical Intern", date(1979,10,25)),
 ("Darius 'Dash' Duvall", "Patient: Status 1A, awaiting a heart", date(1971,8,8)), ("Dr. Natasha Donohue", "Chief of Surgery", date(1958,6,2)),
 ("Dr. Leland Graves", "Chief of Neurosurgery", date(1953,4,18)), ("Lamont 'Monty' Gaines", "Owner, Monty's on Jackson", date(1962,10,10)),
 ("Cedric Hall", "Architect; Monty's partner", date(1965,1,22)), ("Tamika Wardell", "Mother of the Wardell quintuplets", date(1974,9,14)),
 ("Andre Wardell", "Tamika's husband", date(1972,3,27)), ("Dr. Isaiah Crump", "Chief of Pediatric Surgery", date(1944,3,11)),
 ("Raymond 'Big Ray' Toles", "Chief of Security", date(1960,1,1)), ("Dr. Clayton Hartwell", "OB/GYN and Fetal Surgeon", date(1971,3,3)),
 ("Lorna Ellison (on-screen debut)", "Raven's mother", date(1961,3,14)), ("Dr. Camille Toussaint", "Orthopedic Resident", date(1976,7,21)),
 ("Augustin Toussaint", "Camille's father", date(1941,2,9)), ("Mercy", "The House's pit bull puppy (about 12 weeks)", date(2005,9,30)),
]
ALSO = ("<i>Also appearing: TWU picketers, Tamiko (Bernadine's stylist), EMTs, a CT radiologist, an anesthesiologist, an organ procurement coordinator, a helicopter crew, Laurelton neighbors, a St. Albans church bus, "
        "a Salvation Army bell ringer, Amtrak passengers, and the four Wardell quintuplets. Mentioned: Dr. Sylvia Rountree, Roger Toussaint, Judge Theodore Jones, Mayor Bloomberg, Victor Donohue, Dr. Joan Mercer, Cornelius Fairbanks, Malcolm Sloan and Raven's late grandmother.</i>")

MEDIA = [
 ("THE NEW YORK TIMES: \"TRANSIT WORKERS END STRIKE; SERVICE TO RESUME TONIGHT\"", "Thursday, December 22, 2005 (web edition)",
  ["\"The leaders of the city's transit workers union voted this afternoon to send its members back to work, ending a three-day strike that shut down the subways and buses and forced millions of New Yorkers to walk, bike and carpool across the bridges in the cold... Contract talks are to continue.\""]),
 ("NEW YORK DAILY NEWS: \"WALK THIS WAY\" (Tuesday) / \"$1M A DAY\" (Wednesday)", "December 20-21, 2005",
  ["\"Mayor Bloomberg denounced the walkout as 'illegal' and 'selfish'... State Supreme Court Justice Theodore Jones fined the Transport Workers Union $1 million a day, and under the Taylor Law each striker loses two days' pay for every day off the job... Cars entering Manhattan below 96th Street must carry at least four people.\""]),
 ("QueensGraceConfidential (Blogger)", "Thursday, December 22, 2005, 6:20 PM",
  ["<i>\"STRIKE OVER, MIRACLES ON. A 14-year-old got a heart today. Sources say a certain transplant patient on Six (yes, the haircut one) wheeled himself downstairs, IV pole and all, and talked the kid into it with a pair of sneakers. We are not crying, you are crying. "
   "Also: a gospel legend's manager was escorted out of a VIP suite by an intern who sings. Also also: someone saw the security van at the Laurelton Christmas House at 5 PM. Big Ray says it was 'a courier run.' Sure, Ray.\"</i> Comments (1,903)."]),
 ("Cardboard sign on the Peebles lawn, Laurelton", "Thursday, December 22, 2005",
  ["\"EARL'S IN THE HOSPITAL. HE SAYS MERRY CHRISTMAS. PRAY FOR HIS SPLEEN.\""]),
 ("Christmas card: Lillian Divine to Dr. Bryce Kennerly", "Left at the ER desk, December 22, 2005",
  ["\"Merry Christmas, baby. Eat a vegetable. -Mrs. D.\""]),
 ("SMS, Motorola RAZR (Marc Bullock to Amond Baker)", "Thursday, December 22, 2005, 2:38 PM",
  ["<b>Marc:</b> \"STRIKE IS OVER. TWU VOTED TO GO BACK. TRAINS TONIGHT.\""]),
]

CONT = [p("Continuity Sheet: Episode 2x12", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>LORNA ELLISON'S ON-SCREEN DEBUT</b> (44). She arrived at Penn Station on the Palmetto from Savannah at 7:52 PM. It was the first time Raven had seen her in six years ('I don't remember you at twenty'). Arianna and Marc were there. On the LIRR to Hunterspoint Avenue, <b>Raven introduced Arianna as 'mine,'</b> and Lorna thanked Arianna. Lorna is staying in the spare room through Christmas. <b>New canon:</b> Raven's grandmother, who raised her from about age 8, has died; she kept Raven's first-grade Pulaski Elementary paper star in her Bible, and it now tops the 49th Avenue tree. Raven lay under the church lights on Jefferson Street as a child.",
 "<b>The Grey's 2x12 beats:</b> Raven decorated the house from 2 to 5 AM (eleven boxes of ornaments; a Fraser fir). <b>Under the tree:</b> Raven, Marc, Harmony and Mercy lay on the living room floor at 11:41 PM. Earl Peebles, of the 'Laurelton Christmas House' (41,000 lights, 22 years), fell 14 feet while fixing a crooked reindeer. A grade III splenic laceration failed nonoperative management, and Lowery and Raven did a splenectomy. <b>Raven and Big Ray flipped his lights on at 5 PM</b> in the security van (logged as a 'courier run') while Earl listened by phone.",
 "<b>Kamari Fields</b> (14), with a failing Fontan (palliated at age four, six surgeries), <b>refused a heart.</b> Robert and Amond split over it. Robert: 'It only works in somebody who's willing to live with it.' Amond: 'I don't do slow.' <b>Amond told Robert his father bled out holding his hand</b>, the first personal thing he's told him. <b>Dash Duvall wheeled himself down and talked Kamari into it</b>, promising a pair of size 9.5 limited-edition Christmas sneakers. The heart came by helicopter from Pennsylvania (cross-clamp 10:50 AM); Robert and Amond transplanted it. Robert later said Amond is 'the most frightened brave person I've ever trained.' Kamari's mother Nadine prays for Dash's phone to ring.",
 "<b>Lady Bernadine Starks</b>, a gospel star with four Grammys and eleven Stellar Awards, had a bleeding duodenal ulcer from her tour, Goody's powders and her entourage. <b>Harmony threw the entourage out twice</b>, but the ulcer perforated anyway, and Harmony did a Graham patch under Lowery (her second, after Brother Kareem). Bernadine <b>fired her manager of 22 years, Freddie Lyle</b>, for telling the Apollo she'd be 'fine for tomorrow.' Harmony sang 'This Christmas' for her, and Bernadine has invited her to sing at Bethel.",
 "<b>The TWU strike</b> (December 20-22, real): Howard picketed at Queens Village Depot and Lillian fed the line. Howard loses six days' pay under the Taylor Law: 'Somebody stood up for me in 1974.' He drives the 6:15 AM run on December 23. Natasha joked that Camille swears she's no relation to Roger Toussaint. QGH ran carpool vans (Dr. Rountree's discretionary fund), and 22 nurses slept in the hospital. Esther and Kennerly walked the Pulaski Bridge; Kennerly biked from Carroll Gardens. Kennerly's father is in Scottsdale with his third wife. Kennerly got Lillian's second plate, with a Christmas card.",
 "<b>Augustin gave Camille her mother's crystal rosary</b> (the one thing of hers he carried out). Camille gave him a framed 1970s photo of the Hotel Toussaint on Esplanade, found through a Tulane contact. Augustin: 'I don't know how to be a man who is all right with it.' No reconciliation, but it is grace.",
 "<b>Esther and Clayton leave for Mattapan on December 23</b> (Amtrak). Esther's rule one: 'Nobody leaves the table.' Clayton will wear the burgundy tie, because Malcolm always wears a tie to Corinne's. <b>Marc is going to Brookline for Christmas Day dinner at 4</b>, with Mercy. Joan asked Cornelius to 'find a dog bed.' Natasha has a wrapped gift for Marc.",
 "<b>Amond's Grand Rounds (December 20):</b> he read Ms. Tate-Moore's triage note aloud and asked the 41 residents to stand if they'd ever seen a home-medication form. Nobody stood. Whitlow said 'Thank you, Dr. Baker' and left before the questions. Arianna's Step 2 score is due around January 4. She did the glitter on the quints' stockings and taped up Tamika's handmade 'ELIJAH' stocking. Harmony held Amond's hand in the hallway, and he let her. Elxa is at 33 weeks."])
CONT.append(p("Knowledge Tracker (as of December 22, 2005)", H2))
CONT.append(tbl([["Item", "Who knows"],
 ["Raven and Arianna are together", "Now including Lorna"],
 ["Dash's role in Kamari's yes", "Robert, Amond, Raven, Nadine, the blog"],
 ["Raven's grandmother has died", "The housemates, Lorna"],
 ["Robert's 1981 affair (Delphine Ware) and Mariah", "Still secret (not touched this episode)"],
 ["Heir designation", "Still secret"]],
 [2.6*inch, 3.8*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Earl Peebles", "11/30/1947 (58)", "Grade III splenic laceration; delayed rebleed", "Splenectomy (Lowery; Ellison)", "Stable; post-splenectomy vaccines"],
 ["Lady Bernadine Starks", "3/8/1956 (49)", "Bleeding duodenal ulcer (NSAIDs, stress), then perforation", "EGD clip; Graham patch (Lowery; Divine)", "Recovering"],
 ["Kamari Fields", "4/24/1991 (14)", "Failing Fontan circulation", "Orthotopic heart transplant (R. Bullock; Baker)", "Sinus rhythm; extubation December 23"],
 ["Quentin Bascomb", "1/29/1974 (31)", "Left temporal epidural hematoma (cyclist vs. cab)", "Craniotomy and evacuation (Graves; Smilley; Bullock)", "Expected full recovery"],
 ["Darius 'Dash' Duvall", "8/8/1971 (34)", "Status 1A, day 41", "Continuous milrinone", "Waiting"]],
 [1.1*inch, 0.85*inch, 1.75*inch, 1.75*inch, 0.95*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Lorna Ellison</b> (on-screen debut). <b>Earl</b> (b. November 30, 1947) and <b>Dorothy Peebles</b> (b. June 18, 1949) of 226th Street, Laurelton. <b>Lady Bernadine Starks</b> (b. March 8, 1956), her sister <b>Yvonne</b> (b. April 11, 1960), <b>Freddie Lyle</b> (b. July 7, 1953, now fired) and <b>Brother Oliver Pettway</b> (b. October 2, 1961).",
 "<b>Kamari Fields</b> (b. April 24, 1991) and his mother <b>Nadine</b> (b. August 1, 1967), a TWU station agent. <b>Quentin Bascomb</b> (b. January 29, 1974), a Wall Street analyst who bought a bike for the strike."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["The TWU Local 100 strike ran from 3 AM Tuesday, December 20, to Thursday, December 22, 2005, when the union's executive board voted to return to work; service resumed that night and was fully restored by Friday morning. Justice Theodore Jones fined the union $1 million a day, the Taylor Law penalty is two days' pay per strike day, and carpools of four were required to enter Manhattan below 96th Street. "
 "A key issue was the MTA's proposal that new hires contribute more toward pensions. TWU Local 100's president was Roger Toussaint. People walked the Brooklyn, Queensboro, Williamsburg and Pulaski bridges. The LIRR and Amtrak kept running, and the LIRR serves Hunterspoint Avenue in LIC. The Palmetto runs between Savannah and New York.",
 "Medicine: hemodynamically stable grade III splenic injuries without contrast blush are often managed nonoperatively, but they can rebleed and need splenectomy, followed by vaccination against encapsulated organisms. NSAID and aspirin use (including Goody's powders) and H. pylori cause peptic ulcers, and perforation is repaired with a Graham omental patch. "
 "A failing Fontan is an indication for heart transplant, and the leading cause of late graft loss in adolescents is nonadherence. Donor heart ischemic time is ideally under four to six hours. An epidural hematoma (often from the middle meningeal artery) classically shows a lucid interval and needs emergent evacuation."])
