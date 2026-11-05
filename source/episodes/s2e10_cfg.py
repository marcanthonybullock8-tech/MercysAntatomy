import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E10_Much_Too_Much.pdf')
PARTS = [D + 's2e10_part1.txt', D + 's2e10_part2.txt', D + 's2e10_part3.txt']
EP = date(2005, 12, 1)
CODE = '2x10'
SEASON_LINE = 'Season 2, Episode 10'
TITLE = 'Much Too Much'
COUNTERPART = "Episode 2x10. The counterpart of <i>Grey's Anatomy</i> 2x10."
DATES = 'Thursday, December 1, 2005, 5:41 AM through 11:58 PM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x09'
AGES_ON = 'Thursday, December 1, 2005'

CAST = [
 ("Howard Divine", "Harmony's father; MTA Q4 bus operator", date(1950,8,30)), ("Miss Odell Brightwater (new)", "Q4 passenger", date(1927,4,22)),
 ("Raymond 'Big Ray' Toles", "Chief of Security", date(1960,1,1)), ("Dr. Constance Albritton (new)", "Joint Commission physician surveyor", date(1946,9,8)),
 ("Gerald Mayfield, RN (new)", "Joint Commission nurse surveyor", date(1954,5,19)), ("Dolores Haskins (new)", "Joint Commission administrator surveyor", date(1959,1,27)),
 ("Dr. Horace Whitlow", "Chief of Medicine", date(1949,9,19)), ("Dr. Natasha Donohue", "Chief of Surgery", date(1958,6,2)),
 ("Franklin Bassett, Esq.", "General Counsel", date(1958,10,28)), ("Bernadette 'Bernie' Watkins", "Executive Assistant to the Chief", date(1950,6,6)),
 ("Dr. Arianna Cummings", "Surgical Intern (Step 2 CK retake December 12)", date(1979,10,25)), ("Dr. Raven Ellison", "Surgical Intern (26 on Saturday)", date(1979,12,3)),
 ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)), ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)),
 ("Dr. Amond Baker", "Surgical Intern", date(1979,2,10)), ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)),
 ("Dr. Bryce Kennerly", "Surgical Intern (on probation)", date(1978,6,11)), ("Dr. Elxa Bullock", "Surgical Resident (30 weeks pregnant)", date(1977,8,29)),
 ("Dr. Abraham Lowery", "Attending General Surgeon", date(1947,1,9)), ("Jermaine 'Jaws' Biggs (new)", "Patient: acute gastric dilatation, perforation", date(1978,8,20)),
 ("Annette Biggs (new)", "Jermaine's mother; corrections officer", date(1953,11,3)), ("Ambrose Tate (new)", "Patient: digoxin toxicity; retired Pullman porter", date(1926,7,4)),
 ("Celestine Tate-Moore (new)", "Ambrose's daughter; bank manager", date(1955,10,18)), ("Dr. Philip Grant", "Medicine Resident", date(1976,3,13)),
 ("Geraldine Toomer (new)", "Patient: 41-lb ovarian mucinous cystadenoma", date(1953,6,25)), ("Dr. Clayton Hartwell", "OB/GYN and Fetal Surgeon", date(1971,3,3)),
 ("Dr. Camille Toussaint", "Orthopedic Resident", date(1976,7,21)), ("Augustin Toussaint", "Camille's father", date(1941,2,9)),
 ("Lamont 'Monty' Gaines", "Owner, Monty's on Jackson", date(1962,10,10)), ("Cedric Hall", "Architect; Monty's partner", date(1965,1,22)),
 ("Russell Jeffries", "Elxa's husband; chemistry teacher", date(1975,4,3)), ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)),
]
ALSO = ("<i>Also appearing: the QGH CEO, the Chief Nursing Officer, the surgical program director, a CT radiologist, two anesthesiologists, scrub and circulating nurses, a recovery nurse, and a teenage cast patient and his mother. "
        "Mentioned: Rosa Parks, Lorna Ellison (by card), Victor Donohue, Dr. Okafor (Mr. Tate's Harlem cardiologist), Sister Patterson, Corinne Smilley, Malcolm Sloan, Lillian Divine and Dr. Paulette Greenidge.</i>")

MEDIA = [
 ("THE NEW YORK TIMES: \"50 YEARS LATER, A SEAT LEFT EMPTY IN HER HONOR\"", "Thursday, December 1, 2005",
  ["\"Fifty years ago today, Rosa Parks refused to give up her seat on a Montgomery city bus... Transit systems across the country planned to mark the anniversary today by reserving seats in her memory, five weeks after her death at 92...\""]),
 ("ASSOCIATED PRESS: \"VIRGINIA GOVERNOR SPARES INMATE; NATION'S 1,000TH EXECUTION NOW SET FOR NORTH CAROLINA\" / \"TRANSIT UNION, MTA FAR APART AS DEADLINE NEARS\"", "Thursday, December 1, 2005",
  ["\"RICHMOND, Va. (AP) -- Gov. Mark Warner commuted the death sentence of Robin Lovitt on Tuesday...\" / \"NEW YORK (AP) -- The Transport Workers Union and the MTA remained far apart on wages and pensions with the contract set to expire December 16...\""]),
 ("The Joint Commission: Summary of Survey Findings (excerpt)", "Queens Grace Hospital, for-cause survey, December 1, 2005",
  ["\"Complaint: alleged conflict of interest in supervision and evaluation of a resident physician. FINDING: NOT SUBSTANTIATED. Supervision and evaluation appropriate and well documented. Department of Surgery service-assignment firewall (11/9/2005) noted as a leading practice. Universal Protocol: full compliance observed.\"",
   "\"REQUIREMENT FOR IMPROVEMENT -- Department of Medicine: NPSG Goal 8 (accurately and completely reconcile medications across the continuum of care). Tracer patient received duplicate digoxin therapy for approximately 48 hours. Evidence of Standards Compliance due within 45 days.\""]),
 ("QueensGraceConfidential (Blogger)", "Thursday, December 1, 2005, 7:02 PM",
  ["<i>\"THE INSPECTORS HAVE LEFT THE BUILDING. Sources in the boardroom say the complaint against Dr. X was NOT SUBSTANTIATED (we told you). The twist: they found a real problem, in MEDICINE. A man got double heart pills for two days, and guess who caught it? "
   "Dr. X's roommate. A certain Chief of Medicine reportedly 'has no comment.' Also: a 41-pound tumor came out in OR 7 today, and a man ate 174 wings and lost a third of his stomach. Thursday, people.\"</i> Comments (2,071)."]),
 ("Birthday card: Lorna Ellison to Raven Ellison", "Postmarked Savannah, Ga., November 28, 2005",
  ["\"Happy 26th birthday, my Raven. Twenty-six years ago Saturday, I held you in Memorial Hospital and promised I'd be better. I wasn't, for a long time. I am now. If it's not too much, I'd like to see you. Christmas, or whenever you say. If it's too much, I understand. -Mama\" (Raven's reply, written on an envelope: \"CHRISTMAS.\")"]),
 ("SMS, Motorola RAZR (Arianna Cummings to Raven Ellison)", "Thursday, December 1, 2005, 4:09 PM",
  ["<b>Arianna:</b> \"21 over.\"", "<b>Arianna:</b> \"dont say it\"", "<b>Raven:</b> \"less.\"", "<b>Arianna:</b> \"i hate you. k.\""]),
]

CONT = [p("Continuity Sheet: Episode 2x10", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>THE JOINT COMMISSION FOR-CAUSE SURVEY</b> (unannounced, December 1, 2005): Dr. Constance Albritton (physician surveyor), Gerald Mayfield, RN, and Dolores Haskins, using tracer methodology. They ran three tracers, interviewed 19 staff and reviewed 109 surgical cases. <b>Result: the complaint is NOT SUBSTANTIATED.</b> Marc's supervision was 'exemplary,' the Firewall was noted as a leading practice, and the OR showed full Universal Protocol compliance. <b>The Department of Medicine received a Requirement for Improvement</b> (NPSG Goal 8, medication reconciliation) after the Ambrose Tate digoxin error, with Evidence of Standards Compliance due within 45 days. Albritton: 'Complaints often take us places the complainant didn't expect.'",
 "<b>Amond caught the error</b> (xanthopsia, bradycardia of 38, a level of 4.1, treated with Digibind) on a pacemaker consult. Harriet made him recite his grandmother's medicine cabinet every Sunday at age ten. <b>Whitlow's own department is now the one under scrutiny</b>, and the catch came from a 49th Avenue housemate. Natasha told Whitlow: 'You should send him a fruit basket.'",
 "<b>KENNERLY'S SWORN STATEMENT</b> to Bassett says Whitlow told him in September, in his office over tea, that Marc is the Chief's son and Victor's grandson ('from a board member in confidence'). Whitlow said 'make them wonder,' promised a fellowship letter and probation help, and later disowned him. Kennerly's reason: Lillian Divine's Thanksgiving plate. He told surveyor Haskins that Marc received no preferential treatment ('He's better than me'). <b>Natasha had the statement sealed in the General Counsel's safe</b> and won't use it at the December 15 board meeting: 'The day I use it, I become him... I'd like to still have one left.' Robert knows. Kennerly remains on probation, and he and Marc shared a beer at Monty's.",
 "<b>Marc's interview with Albritton:</b> he asked Natasha to reverse the Firewall at the kitchen table, and she sent him to Lowery, who said no. 'When my hands are inside somebody, nobody in the room cares whose grandson I am.' Albritton (Meharry, 1971) was steered away from surgery toward 'gentler hands' and became an internist out of spite. To Marc: 'Your hands are your own.' Lowery to Albritton: 'Favors kill people.' Lowery trained at Kings County.",
 "<b>Camille and Augustin:</b> in the chapel, Augustin confirmed he saw them in the kitchen. Camille's mother suspected when Camille was 16 ('that girl from Ursuline'). Augustin: 'Don't bring her to my table.' He does not accept it, per MA-005. <b>Harmony and Camille spent their first night together</b> at Camille's apartment. Harmony told Camille about Howard's nodule. Camille hadn't known about her father until today.",
 "<b>Raven's mother:</b> Lorna's birthday card asks to visit 'Christmas, or whenever you say.' <b>Raven answered 'CHRISTMAS.'</b> Marc almost flew Lorna up for a surprise party, and Amond stopped him. Raven's birthday (Saturday, December 3) will be a <b>small</b> roof-deck party with a one-tier red velvet cake from Make My Cake. Raven has never had a birthday party. Raven does Geraldine Toomer's hair.",
 "<b>Arianna:</b> she was sleeping three hours a night with 11 days to go. Raven locked her flashcards away and fed her. Her practice NBME came back <b>21 points above passing</b>. The retake is December 12. Raven: 'less.'",
 "<b>Esther</b> wants to go to Mattapan for Christmas with Clayton, and <b>she will ask Corinne to invite Malcolm</b>: 'I'm not forgiving him. I'm just not going to be the reason there's an empty chair.' Clayton is shaken. More of Esther's things are now at Remsen Street.",
 "<b>Elxa (30 weeks):</b> Lamaze starts Monday, December 5. Russell bought a purple birthing ball and coaches her breathing. Russell: 'Tell him February. Super Bowl.' (Tuck is born on Super Bowl Sunday, February 5, 2006, per MA-005.) Natasha cried on the phone to Elxa for the first time since Elxa's wedding. Robert's rocking chair had one leftover screw. Victor offered to call 'a man he knows at the Commission,' and Natasha threatened to bar him from the building.",
 "<b>Howard Divine</b> tied a black ribbon on the seat behind him on the Q4 for the Rosa Parks anniversary and kept it in his breast pocket. His cough persists, and the CT is on Thursday, December 8."])
CONT.append(p("Knowledge Tracker (as of December 1, 2005)", H2))
CONT.append(tbl([["Item", "Who knows"],
 ["Whitlow planted the rumor (Kennerly's statement)", "Kennerly, Bassett, Natasha, Robert; sealed in the GC's safe"],
 ["JC findings", "Leadership, the board (formal report), everyone (via the blog)"],
 ["Harmony and Camille", "Housemates, Augustin (confirmed, rejecting), Grace (likely)"],
 ["Lorna visiting at Christmas", "Raven, Marc, Amond, Arianna"],
 ["Esther will invite Malcolm to Christmas", "Esther, Clayton"],
 ["Heir designation", "Still secret: Victor, Marc, V.J., the Foundation board, Natasha and Joan"]],
 [2.6*inch, 3.8*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Jermaine 'Jaws' Biggs", "8/20/1978 (27)", "Acute gastric dilatation after an eating contest (174 wings), necrosis and perforation", "NG decompression; laparotomy, wedge resection of the greater curvature, washout, feeding jejunostomy (Lowery; Bullock; Smilley)", "Recovering; no more contests"],
 ["Ambrose Tate", "7/4/1926 (79)", "Digoxin toxicity (level 4.1) from home plus hospital digoxin; no med reconciliation", "Digoxin immune fab (Baker; Medicine)", "Recovered; HR 64"],
 ["Geraldine Toomer", "6/25/1953 (52)", "34 x 29 cm ovarian mucinous cystadenoma, 41 lb 4 oz", "Laparotomy, intact removal (Hartwell; Ellison)", "Benign; she can see her feet"],
 ["Teen forearm fracture", "-", "Forearm fracture", "Fiberglass cast (Toussaint; Divine)", "Discharged"]],
 [1.1*inch, 0.85*inch, 1.75*inch, 1.75*inch, 0.95*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Dr. Constance Albritton</b> (b. September 8, 1946; Meharry), <b>Gerald Mayfield, RN</b> (b. May 19, 1954) and <b>Dolores Haskins</b> (b. January 27, 1959): Joint Commission surveyors. <b>Miss Odell Brightwater</b> (b. April 22, 1927), a Q4 rider.",
 "<b>Jermaine Biggs</b> (b. August 20, 1978), the 2005 Sutphin Boulevard 'Wing King,' and his mother <b>Annette</b> (b. November 3, 1953), a Rikers corrections officer. <b>Ambrose Tate</b> (b. July 4, 1926), who carried bags for 41 years on the Twentieth Century Limited and the Broadway Limited, and his daughter <b>Celestine Tate-Moore</b> (b. October 18, 1955). <b>Geraldine Toomer</b> (b. June 25, 1953), organist at Greater Allen A.M.E."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["December 1, 2005 was the 50th anniversary of Rosa Parks's arrest on a Cleveland Avenue bus in Montgomery (she died October 24, 2005). Transit agencies marked it by reserving seats in her honor. On November 29, 2005, Virginia Gov. Mark Warner commuted Robin Lovitt's death sentence, so the nation's 1,000th execution since 1976 fell to North Carolina (Kenneth Lee Boyd, December 2). "
 "The TWU Local 100 contract expired December 16, 2005, and the strike began December 20. The Pennsylvania Railroad's Broadway Limited and the New York Central's 20th Century Limited were famous Pullman trains. 'Total Praise' is by Richard Smallwood (1996).",
 "The Joint Commission: tracer methodology began in 2004 ('Shared Visions-New Pathways'). For-cause unannounced surveys respond to complaints. National Patient Safety Goal 8 (medication reconciliation) took effect in 2005, with full implementation expected by January 2006. A Requirement for Improvement requires Evidence of Standards Compliance within 45 days. The Universal Protocol (time-out) took effect July 2004.",
 "Medicine: acute gastric dilatation after binge eating can cause ischemic necrosis and perforation, and needs NG decompression and resection if necrotic. Digoxin toxicity causes nausea, confusion, bradyarrhythmias and xanthopsia (yellow vision), and is treated with digoxin immune fab. "
 "Mucinous cystadenomas can grow to massive size and should be removed intact to avoid spillage (pseudomyxoma peritonei). Relieving vena caval compression can cause abrupt hemodynamic shifts."])
