import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E08_Let_It_Be.pdf')
PARTS = [D + 's2e8_part1.txt', D + 's2e8_part2.txt', D + 's2e8_part3.txt']
EP = date(2005, 11, 9)
CODE = '2x08'
SEASON_LINE = 'Season 2, Episode 8'
TITLE = 'Let It Be'
COUNTERPART = "Episode 2x08. The counterpart of <i>Grey's Anatomy</i> 2x08."
DATES = 'Wednesday, November 9, 2005, 5:14 AM through 11:48 PM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x07'
AGES_ON = 'Wednesday, November 9, 2005'

CAST = [
 ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)), ("Dr. Arianna Cummings", "Surgical Intern", date(1979,10,25)),
 ("Dr. Natasha Donohue", "Chief of Surgery", date(1958,6,2)), ("Franklin Bassett, Esq.", "General Counsel", date(1958,10,28)),
 ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)), ("Dr. Amond Baker", "Surgical Intern", date(1979,2,10)),
 ("Dr. Raven Ellison", "Surgical Intern", date(1979,12,3)), ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)),
 ("Dr. Bryce Kennerly", "Surgical Intern (on probation)", date(1978,6,11)), ("Dr. Elxa Bullock", "Surgical Resident (26 weeks 5 days pregnant)", date(1977,8,29)),
 ("Mother Cornelia Haynes (new)", "Patient: pancreatic head mass; retired Harlem Hospital nurse", date(1924,3,2)), ("Deborah Haynes-Price (new)", "Cornelia's daughter; vice principal", date(1950,5,17)),
 ("Brandon Haynes-Price (new)", "Cornelia's grandson; nursing student", date(1983,7,8)), ("Dr. Abraham Lowery", "Attending General Surgeon", date(1947,1,9)),
 ("Nurse Gloria Pettiford", "Head ER Nurse", date(1952,4,14)), ("Dr. Camille Toussaint", "Orthopedic Resident", date(1976,7,21)),
 ("Deacon Otis 'Bulldog' Merriweather (new)", "Patient: displaced femoral neck fracture", date(1944,8,14)), ("Mavis Merriweather (new)", "Otis's wife", date(1946,2,27)),
 ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)), ("Dr. Leland Graves", "Chief of Neurosurgery", date(1953,4,18)),
 ("Hattie 'Miss Hattie' Lomax", "Cafeteria", date(1945,3,3)), ("Dr. Horace Whitlow", "Chief of Medicine", date(1949,9,19)),
 ("Russell Jeffries", "Elxa's husband; chemistry teacher", date(1975,4,3)), ("Bernadette 'Bernie' Watkins", "Executive Assistant to the Chief", date(1950,6,6)),
 ("Winston Teague (new)", "Patient: end-stage heart failure, LVAD", date(1947,1,22)), ("Pauline Teague (new)", "Winston's wife", date(1950,9,30)),
 ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)), ("Lamont 'Monty' Gaines", "Owner, Monty's on Jackson", date(1962,10,10)),
 ("Cedric Hall", "Architect; Monty's partner", date(1965,1,22)), ("Simone Bracey (new)", "Patient: colloid cyst, hydrocephalus", date(1986,2,11)),
 ("Lester Grimes (new)", "Patient: ACE-inhibitor angioedema", date(1939,6,3)), ("Dr. Yolanda Fitch (new)", "ER Attending", date(1961,5,12)),
 ("Dr. Harold Bynum (new)", "Consult-Liaison Psychiatrist", date(1942,10,19)), ("Gail Bracey (new)", "Simone's mother", date(1959,8,4)),
 ("Dr. Clayton Hartwell", "Fetal Surgeon; Esther's husband", date(1971,3,3)), ("Dr. Paulette Greenidge", "Couples therapist, Brooklyn Heights", date(1955,8,1)),
 ("Dr. Malcolm Sloan (V.O., voicemail)", "Plastic Surgeon, Boston", date(1968,2,14)),
]
CAST = [c for i, c in enumerate(CAST) if c[0] not in [x[0] for x in CAST[:i]]]
ALSO = ("<i>Also appearing: a CT radiologist, a GI attending, Mr. Kostas (the baker, off-screen), Mrs. Grimes, an anesthesiologist, scrub and circulating nurses, a CVICU nurse and the lunch crowd at Monty's. "
        "Mentioned: Lorna Ellison (by letter), Augustin Toussaint (by phone), Corinne Smilley, Josephine Bullock (by note), Victor Donohue, Grace Bullock, Howard Divine, Paul Tergat, Hendrick Ramaala, "
        "Dr. Martin Luther King Jr., and Drs. Aubre de L. Maynard, John W. V. Cordice and Emil Naclerio.</i>")

MEDIA = [
 ("THE NEW YORK TIMES: \"BLOOMBERG CRUISES TO SECOND TERM, ROUTING FERRER\"", "Wednesday, November 9, 2005",
  ["\"Mayor Michael R. Bloomberg won a second term last night by one of the widest margins in the city's history, defeating Fernando Ferrer by roughly 20 percentage points...\""]),
 ("ASSOCIATED PRESS: \"BOMBS ROCK THREE HOTELS IN JORDAN'S CAPITAL\"", "Wednesday, November 9, 2005",
  ["\"AMMAN, Jordan (AP) -- Near-simultaneous explosions struck three hotels in the Jordanian capital Wednesday night, one of them during a wedding reception, killing dozens...\" Also on the wire: France's state of emergency in its rioting suburbs (declared Tuesday); Dover, Pa., voters ousted the school board members who backed intelligent design; Kansas's school board adopted science standards that question evolution."]),
 ("NEW YORK DAILY NEWS (Sports): \"PHOTO FINISH! TERGAT NIPS RAMAALA\"", "Monday, November 7, 2005",
  ["\"Paul Tergat of Kenya won the New York City Marathon by a fraction of a second over South Africa's Hendrick Ramaala, the closest finish in race history, as Jelena Prokopcuka of Latvia won the women's race...\""]),
 ("QueensGraceConfidential (Blogger)", "Wednesday, November 9, 2005, 6:12 PM",
  ["<i>\"FIREWALL. Word from the fifth floor: Dr. X is OFF Cardio and OFF OB for the rest of the year, by order of his own mother. Whatever you think of the family, that's not what favoritism looks like, people. "
   "Also: a certain probationary intern (Dr. K, you know who you are) did a surgical airway in under 90 seconds in Trauma 2 today. Our ER source says Nurse P. gave him a towel. Nurse P. does not give towels. Also also: the Monopoly cards in lockers stop NOW. It's not funny anymore. It was barely funny on Monday.\"</i> Comments (612)."]),
 ("SMS, Motorola RAZR (Raven Ellison to Arianna Cummings)", "Wednesday, November 9, 2005, 5:58 AM and 7:51 PM",
  ["<b>Raven (5:58 AM):</b> \"its wednesday. call me.\"", "<b>Raven (5:59 AM):</b> \"or text k. i'll take k.\"", "<b>Arianna (7:51 PM):</b> \"monty's. bring the purple ones.\""]),
 ("Letter: Lorna Ellison to Raven Ellison", "Postmarked Savannah, Ga., January 2003 (opened November 9, 2005)",
  ["\"Raven. Today is thirty days. They gave me a chip. It's red. I don't know what to do with it, so I'm sending it to you. I'm not asking you for anything. I don't have the right. I just wanted you to know your mama is somewhere today with a clear head, thinking about you. -Lorna\" (Enclosed: one red 30-day chip.)"]),
 ("Joint Commission correspondence (excerpt)", "Received by QGH General Counsel, Tuesday, November 8, 2005, 9:04 PM",
  ["\"...The Office of Quality Monitoring has received a complaint regarding potential conflicts of interest in the supervision and evaluation of a resident physician related to members of hospital leadership... The organization is requested to provide a written response... The Joint Commission reserves the right to conduct an unannounced for-cause survey.\""]),
]

CONT = [p("Continuity Sheet: Episode 2x08", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>The Joint Commission complaint has arrived.</b> A courier delivered it to Bassett's home at 9 PM on November 8. It is anonymous, but it uses the word 'nepotistic,' so it's Whitlow. The Office of Quality Monitoring wants a written response and reserves the right to an unannounced for-cause survey. Natasha's strategy is to <b>'let it be':</b> no fight with Whitlow, no calls to the board or the Commission, every chart open. Bassett points out that a for-cause survey walks every department, <b>Medicine included</b>. Natasha forbids pointing at it. She told Whitlow in the garage: 'Let them come.'",
 "<b>THE FIREWALL:</b> effective November 9, Marc will not rotate on, take call for, or be evaluated by Cardiothoracic or OB/GYN for the rest of his intern year. Elxa won't evaluate him either. His evaluations are written by Lowery, Crump and Graves and countersigned by the program director. Bassett's audit covers Marc's 109 cases since July 1: Robert attended 11 and Natasha 2 (both deliveries, with Clayton present). 'The cleanest file I've ever seen on an intern.' Esther came off Clayton's service on Monday, November 7, at her own request.",
 "<b>Marc called Robert 'Dad' out loud</b> on the hospital roof. Robert asked to come to Thanksgiving. <b>Thanksgiving at 49th Avenue (November 24) now includes Victor (with a pie he won't bake), Natasha, Robert and Grace</b>, plus the housemates. Amond insists on buying a gravy boat. Harmony's mother's macaroni and cheese. Raven is making Savannah dressing. Arianna will study at the table.",
 "<b>Arianna failed USMLE Step 2 CK</b> by three points (her school didn't require it to graduate; she took it in the second week of October). Her earliest retake is <b>December 12, 2005</b> (60 days). QGH doesn't issue PGY-2 contracts without a pass. Raven made her color-coded flashcards (purple is biostatistics, 'the color of suffering'), and Monty delivered them. Arianna: 'Quiz me.'",
 "<b>Raven opened letter #1 of 34</b>, postmarked January 2003, from her mother, <b>Lorna Ellison</b>. It held a red 30-day chip. Thirty-three letters remain unopened. Arianna was with her. Marc knows Raven opened one.",
 "<b>Harmony and Camille:</b> first dinner at Camille's apartment off 37th Avenue in Jackson Heights (gumbo in her grandmother's pot, one of six things saved from the house on Elysian Fields). <b>Augustin Toussaint</b> is sleeping on a cousin's couch in Canarsie. He lost 40 buildings, a hotel and his wife's grave to the flood. Camille told him Harmony is 'just a friend from work' and isn't ready to come out to him. They kissed by the stove.",
 "<b>Esther and Clayton, session eight</b> with Dr. Greenidge (Montague Street). Malcolm left a voicemail on Monday, November 7: he isn't taking the NYU job, and for the first time in 27 years he told Corinne Smilley no for Thanksgiving. Esther played it on speaker and then deleted it: 'Now it's a decision.'",
 "<b>Kennerly</b> did a surgical cricothyrotomy in under 90 seconds on Lester Grimes (ACE-inhibitor angioedema). Gloria gave him a towel and later a coffee. Whitlow disowned him ('We don't really know each other, do we?') and denied promising him a fellowship letter. <b>Kennerly now knows he was used.</b> Someone keeps putting Monopoly cards in Marc's locker.",
 "<b>Elxa and Russell</b> are enrolled in Lamaze at Jamaica Hospital, Monday nights from December 5. Russell teaches chemistry at August Martin High School. <b>Graves's backstory:</b> at 18 he left Durham on a Trailways bus with eleven dollars and a letter from Victor Donohue."])
CONT.append(p("Knowledge Tracker (as of November 9, 2005)", H2))
CONT.append(tbl([["Item", "Who knows"],
 ["Marc's parentage", "Effectively everyone at QGH; Deborah Haynes-Price (patient family) heard it from a nurse"],
 ["Whitlow wrote the JC complaint", "Natasha, Bassett, Elxa (suspected); Kennerly (certain); not provable"],
 ["Heir designation (2001 will)", "Still secret: Victor, Marc, V.J., the Foundation board and Natasha"],
 ["Arianna failed Step 2 CK", "Raven; Monty (by inference)"],
 ["Raven's mother is alive", "Arianna, Marc (told in the endoscopy suite); Raven has opened 1 of 34 letters"],
 ["Malcolm's voicemail", "Esther, Clayton, Dr. Greenidge (deleted)"]],
 [2.6*inch, 3.8*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Mother Cornelia Haynes", "3/2/1924 (81)", "3.1 cm pancreatic head mass, double duct sign, resectable", "Declined Whipple; capacity confirmed (Bynum); ERCP biliary stent", "Itching resolved; going home for comfort care"],
 ["Deacon Otis Merriweather", "8/14/1944 (61)", "Displaced (Garden IV) femoral neck stress fracture after the marathon", "Total hip arthroplasty (Toussaint; Divine)", "Up Thursday, home Friday expected"],
 ["Winston Teague", "1/22/1947 (58)", "Ischemic cardiomyopathy, EF 12%, transplant-ineligible", "HeartMate XVE LVAD, destination therapy (R. Bullock; Baker)", "Post-op RV failure caught by Baker; milrinone and iNO; stable"],
 ["Simone Bracey", "2/11/1986 (19)", "Colloid cyst, third ventricle, obstructive hydrocephalus", "Transcallosal resection (Graves; Smilley opened)", "Neurologically intact"],
 ["Lester Grimes", "6/3/1939 (66)", "ACE-inhibitor (lisinopril) angioedema, failed fiberoptic", "Emergent cricothyrotomy (Kennerly)", "Airway secured; lisinopril discontinued"],
 ["Scalp laceration (Bay 9)", "-", "Laceration, intoxication", "Repair (Kennerly)", "Discharged"]],
 [1.1*inch, 0.85*inch, 1.75*inch, 1.75*inch, 0.95*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Mother Cornelia Haynes</b> (b. March 2, 1924), a Harlem Hospital nurse from 1947 to 1991 and a church mother at Abyssinian since 1979. She lives in Sugar Hill. <b>Deborah Haynes-Price</b> (b. May 17, 1950), a vice principal, whom Cornelia delivered herself. <b>Brandon Haynes-Price</b> (b. July 8, 1983), a Hunter-Bellevue nursing student who pins in May 2006.",
 "<b>Deacon Otis 'Bulldog' Merriweather</b> (b. August 14, 1944), who has run 20 NYC Marathons, and <b>Mavis</b> (b. February 27, 1946). <b>Winston Teague</b> (b. January 22, 1947), a jazz drummer, and <b>Pauline</b> (b. September 30, 1950); their granddaughter marries at Riverside Church in June 2006.",
 "<b>Simone Bracey</b> (b. February 11, 1986), a Queens College sophomore and poet, and her mother <b>Gail</b> (b. August 4, 1959). <b>Lester Grimes</b> (b. June 3, 1939). <b>Dr. Yolanda Fitch</b> (b. May 12, 1961), ER attending. <b>Dr. Harold Bynum</b> (b. October 19, 1942), consult-liaison psychiatry.",
 "<b>Lorna Ellison</b>, Raven's mother, is named for the first time (by letter only). Cedric Hall (b. January 22, 1965, per MA-005) appears."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["November 8, 2005: Bloomberg defeated Ferrer by about 20 points; Dover, Pennsylvania voters removed the pro-intelligent-design school board; the Kansas Board of Education adopted standards critical of evolution; France declared a state of emergency over the suburban riots. "
 "November 9, 2005: suicide bombings struck the Radisson SAS, Grand Hyatt and Days Inn hotels in Amman, Jordan, around 8:50 PM local time (about 1:50 PM in New York), one of them during a wedding reception. On November 6, 2005, Paul Tergat beat Hendrick Ramaala in the New York City Marathon's closest finish, and Jelena Prokopcuka won the women's race. USMLE scores were customarily released on Wednesdays, and a retake required a 60-day wait.",
 "On September 20, 1958, Dr. Martin Luther King Jr. was stabbed with a letter opener by Izola Ware Curry while signing <i>Stride Toward Freedom</i> at Blumstein's department store on 125th Street. At Harlem Hospital, Drs. Aubre de L. Maynard, John W. V. Cordice and Emil Naclerio removed the blade, whose tip lay against his aorta. King later recalled a letter from a girl who was glad he 'didn't sneeze.' Cornelia's presence (on the floor upstairs, not in the OR) is fictional.",
 "Medicine: painless jaundice with a pancreatic head mass and a 'double duct sign' suggests adenocarcinoma. Whipple mortality and morbidity rise with age, and palliative ERCP stenting relieves jaundice and pruritus. A health care proxy takes effect only when the patient lacks capacity; capacity is assessed on four criteria (choice, understanding, appreciation and reasoning). "
 "Displaced femoral neck fractures in active older adults are commonly treated with total hip arthroplasty because of the risk of avascular necrosis. The HeartMate XVE was FDA-approved for destination therapy in November 2002, based on REMATCH (one-year survival 52% vs. 25%). Right ventricular failure after LVAD is treated with inotropes, inhaled nitric oxide and a lower pump speed. "
 "Colloid cysts of the third ventricle can cause sudden death, and the transcallosal approach risks the fornices. ACE-inhibitor angioedema occurs three to five times more often in Black patients and can require a surgical airway."])
