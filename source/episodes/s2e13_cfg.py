import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E13_Brand_New_Day.pdf')
PARTS = [D + 's2e13_part1.txt', D + 's2e13_part2.txt', D + 's2e13_part3.txt']
EP = date(2006, 1, 11)
CODE = '2x13'
SEASON_LINE = 'Season 2, Episode 13'
TITLE = 'Brand New Day'
COUNTERPART = "Episode 2x13. The counterpart of <i>Grey's Anatomy</i> 2x13 (the midseason premiere)."
DATES = 'Wednesday, January 11, 2006, 5:02 AM through 11:58 PM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x12'
AGES_ON = 'Wednesday, January 11, 2006'

CAST = [
 ("Dr. Arianna Cummings", "Surgical Intern (passed Step 2 CK)", date(1979,10,25)), ("Dr. Raven Ellison", "Surgical Intern", date(1979,12,3)),
 ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)), ("Dr. Amond Baker", "Surgical Intern", date(1979,2,10)),
 ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)), ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)),
 ("Dr. Elxa Bullock", "Surgical Resident (35 weeks 6 days pregnant)", date(1977,8,29)), ("Dr. Natasha Donohue", "Chief of Surgery", date(1958,6,2)),
 ("Dr. Bryce Kennerly", "Surgical Intern (probation review)", date(1978,6,11)), ("Silas Tillman (new)", "Patient: symptomatic, then ruptured, AAA", date(1920,9,2)),
 ("Corinthia Tillman (new)", "Silas's wife of 60 years", date(1923,5,15)), ("Dr. Wendell Moseley (new)", "Chief of Vascular Surgery", date(1944,8,25)),
 ("Keisha Bowman (new)", "Patient: exertional rhabdomyolysis, bilateral compartment syndrome", date(1967,10,9)), ("Dr. Camille Toussaint", "Orthopedic Resident", date(1976,7,21)),
 ("Darius 'Dash' Duvall", "Patient: Status 1A, day 61", date(1971,8,8)), ("Glenda Duvall (new)", "Dash's mother", date(1947,12,12)),
 ("Kamari Fields", "Transplant recipient (discharged)", date(1991,4,24)), ("Nadine Fields", "Kamari's mother", date(1967,8,1)),
 ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)), ("Franklin Bassett, Esq.", "General Counsel", date(1958,10,28)),
 ("Dr. Sylvia Rountree (on-screen debut)", "President and CEO, Queens Grace Hospital", date(1951,12,2)), ("Dr. Horace Whitlow", "Chief of Medicine", date(1949,9,19)),
 ("Lamont 'Monty' Gaines", "Owner, Monty's on Jackson", date(1962,10,10)), ("Nurse Gloria Pettiford", "Head ER Nurse", date(1952,4,14)),
 ("Dr. Abraham Lowery", "Attending General Surgeon", date(1947,1,9)), ("Dr. Eugene Pratt (new)", "Surgical Program Director", date(1948,11,14)),
 ("Dr. Clayton Hartwell", "OB/GYN and Fetal Surgeon", date(1971,3,3)), ("Rev. Dr. Elias Montgomery (new)", "Associate pastor, Abyssinian", date(1937,6,30)),
 ("Mercy", "The House's pit bull puppy (about 4 months)", date(2005,9,30)), ("Troy Daniels (new)", "Spin instructor, Peak Fitness", date(1974,7,19)),
]
ALSO = ("<i>Also appearing: Mr. Kostas (off-screen), a CT tech, an anesthesiologist, ICU and CVICU nurses, the Tillman family (two sons, a daughter and four grandchildren), Jamaica neighbors, a taverna waiter and a maintenance worker. "
        "Mentioned: Malcolm Sloan, Corinne Smilley, Dr. Joan Mercer, V.J. Donohue, Wanda Moseley (d. 2002), Russell Jeffries, a guard named Alphonse, and Augustin Toussaint.</i>")

MEDIA = [
 ("ASSOCIATED PRESS: \"ALITO HEARINGS ENTER THIRD DAY\" / \"SHARON REMAINS IN COMA\"", "Wednesday, January 11, 2006",
  ["\"WASHINGTON (AP) -- Supreme Court nominee Samuel Alito faced a third day of questioning before the Senate Judiciary Committee...\" / \"JERUSALEM (AP) -- Israeli Prime Minister Ariel Sharon remained in a medically induced coma one week after a massive stroke...\" Also: West Virginia mourned the 12 miners killed in the January 2 Sago Mine explosion."]),
 ("QUEENS GRACE HOSPITAL -- Department of Surgery Memorandum S-06-01", "Effective January 11, 2006",
  ["\"RELATIONSHIPS WITHIN THE TRAINING HIERARCHY. Any attending, fellow or senior resident in a romantic or familial relationship with a trainee in their reporting line must disclose it in writing to the Program Director. The trainee will be reassigned outside that reporting line. No exceptions. -- N. Donohue, M.D., Chief of Surgery\""]),
 ("QueensGraceConfidential (Blogger)", "Wednesday, January 11, 2006, 5:10 PM",
  ["<i>\"VOWS IN THE ICU. An 85-year-old ruptured his aorta in CT this morning, got a new one by noon, and renewed his wedding vows at THREE O'CLOCK SHARP with a breathing tube in. He said yes by blinking. We have never been more emotionally destroyed by a vascular case. "
   "Also: a certain intern got off probation today wearing a tie the whole ER recognizes. And a brass nameplate went up in Plastics tonight. Big name from Boston. Start date February. We have QUESTIONS.\"</i> Comments (2,244)."]),
 ("NBME score report (excerpt): Arianna Cummings", "Posted Wednesday, January 11, 2006",
  ["\"USMLE Step 2 Clinical Knowledge. Test date: December 12, 2005. RESULT: PASS.\" (Twenty-four points above the minimum. Arianna slid a copy, in a plastic sheet protector, under Elxa's door at 6:15 AM.)"]),
 ("SMS, Motorola RAZR (Arianna Cummings to Raven Ellison)", "Wednesday, January 11, 2006, 8:04 PM",
  ["<b>Arianna:</b> \"congratulations to me.\""]),
 ("Brass nameplate, Plastic Surgery Suite, Queens Grace", "Installed Wednesday, January 11, 2006, 8:37 PM",
  ["\"MALCOLM SLOAN, M.D., F.A.C.S. -- CHIEF, DIVISION OF PLASTIC AND RECONSTRUCTIVE SURGERY\""]),
]

CONT = [p("Continuity Sheet: Episode 2x13", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>ARIANNA PASSED STEP 2 CK</b> (24 points above the line; scores posted Wednesday, January 11). Elxa called the program director, and <b>her PGY-2 contract is in her box by Friday.</b> Elxa: 'You didn't hide. Not once.' Raven's dinner at Taverna Kyclades on Ditmars (7 PM) went badly: <b>Raven never arrived</b> because Dash's ICD fired twice at 5:41 PM. She didn't look at her phone until 8:09. Arianna texted 'congratulations to me.' Marc called Arianna at 8:30 to tell her where Raven was. Arianna: 'I'm mad that, while you were staying, you didn't think about me even once.' They ate cold octopus at 11:39 PM, and Raven gave her a silver kidney keychain.",
 "<b>MALCOLM SLOAN IS COMING TO QUEENS GRACE</b> as Chief of Plastic and Reconstructive Surgery, starting in <b>February 2006</b>. Dr. Rountree recruited him; he interviewed in November. He's ex-MGH, Chief of Facial Plastics at 34, with 91 publications. He told Esther on Christmas Eve on Corinne's porch, after the dinner (rule one held; Corinne made him say grace, and he couldn't finish). <b>He listed Clayton as a reference.</b> Clayton gave it in October and confirmed it in November without telling Esther. Malcolm had called Clayton drunk at 2 AM outside Corinne's: 'I want to be where she is.' Esther: 'No more Octobers.' Esther told Natasha: 'Hire him if he's the best.' His nameplate went up at 8:37 PM.",
 "<b>New Department of Surgery policy</b> (Memo S-06-01, January 11): relationships within a reporting line must be disclosed and the trainee reassigned. Natasha publicly confirmed that Esther and Clayton have complied since November. Natasha and Robert expect 'somebody's going to throw a punch.'",
 "<b>Dash Duvall, day 61:</b> his mother <b>Glenda Duvall</b> (58) arrived from Charlotte by Amtrak. His father died at 51 of a heart attack on the loading dock at the Philip Morris plant in Concord, NC. Dash had rheumatic fever at seven, and his cardiomyopathy is idiopathic. Glenda told Raven: 'My son is in love with you.' <b>Dash told Raven he loves her and first called her 'Raven.'</b> Raven: 'I'm with somebody.' <b>An electrical storm (two ICD shocks) moved him to the CVICU</b> on amiodarone and lidocaine. Robert raised an <b>LVAD as a bridge</b> if he storms again.",
 "<b>Kennerly's probation was lifted</b> (92 days) on recommendations from Lowery, Elxa and a two-page letter from Gloria, the first Gloria has ever written <i>for</i> an intern. Gloria gave him her late husband's never-worn Christmas 2003 tie, and Monty taught him a Windsor knot. To Marc: 'I was wrong. About why you're good. It was a correction.'",
 "<b>Robert offered Amond first authorship</b> on a study of 42 adolescent heart recipients at four New York centers since 1995. <b>Whitlow thanked Amond</b> in the elevator. The NPSG 8 Evidence of Standards Compliance went in four days early, the form has been live since December 26, and pharmacy caught 22 errors in 16 days. Whitlow's chief resident wrote 'Tate-Moore' in the margin of every copy. Kamari went home to 168th Street in Jamaica in Dash's sneakers and photographed them on the sidewalk for Dash.",
 "<b>Elxa's leave:</b> desk duty from January 30. Natasha revealed she <b>went into labor with Marc on the steps of Widener Library in January 1979</b> and was caught by a guard named Alphonse; she has never told anyone else. Marc's Christmas in Brookline had 34 Donohues; Joan fed Mercy off the good china: 'Everyone at this table is a rescue, Victor Junior.' <b>Augustin moves into a FEMA-voucher one-bedroom on Halsey Street, Bed-Stuy, on Saturday, January 14</b>, and asked Camille to 'bring a friend with a truck.' Jerry and Ronnie are bringing the truck.",
 "<b>The Tillmans</b> renewed their vows in the SICU at 3:00 PM, the 60th anniversary of their January 11, 1946 wedding at Abyssinian. Silas said yes by blinking. Marc held Esther's hand during the hymn, and she let go when it ended. Moseley's wife Wanda died in 2002."])
CONT.append(p("Knowledge Tracker (as of January 11, 2006)", H2))
CONT.append(tbl([["Item", "Who knows"],
 ["Malcolm hired at QGH", "Natasha, Rountree, Bassett, Robert, Esther, Clayton, Marc; the blog (no name)"],
 ["Malcolm and Clayton's affair", "Esther, Clayton, Malcolm, Marc, Dr. Greenidge (Natasha suspects)"],
 ["Dash loves Raven", "Dash, Glenda, Raven, Arianna, Robert"],
 ["Natasha's Widener Library labor", "Elxa only"],
 ["Heir designation; Robert and Delphine Ware", "Still secret"]],
 [2.6*inch, 3.8*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Silas Tillman", "9/2/1920 (85)", "7.2 cm symptomatic AAA, ruptured in CT (retroperitoneal)", "Open repair, 18 mm tube graft; supraceliac compression by Bullock (Moseley; Bullock; Smilley)", "Awake; vows renewed; ICU"],
 ["Keisha Bowman", "10/9/1967 (38)", "Exertional rhabdomyolysis (CK 112,000), bilateral calf compartment syndrome", "Four-compartment fasciotomies, both legs (Toussaint; Divine)", "Muscle viable; IV fluids for her kidneys"],
 ["Darius 'Dash' Duvall", "8/8/1971 (34)", "DCM, Status 1A; VT storm with two ICD shocks", "Amiodarone and lidocaine; CVICU (R. Bullock; Ellison)", "Stable; LVAD bridge discussed"],
 ["Kamari Fields", "4/24/1991 (14)", "Heart transplant recipient", "Biopsy grade 0; discharge (R. Bullock; Baker)", "Home"]],
 [1.1*inch, 0.85*inch, 1.75*inch, 1.75*inch, 0.95*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Dr. Wendell Moseley</b> (b. August 25, 1944), Chief of Vascular Surgery, widower. <b>Dr. Eugene Pratt</b> (b. November 14, 1948), Surgical Program Director (20 years). <b>Glenda Duvall</b> (b. December 12, 1947). <b>Dr. Sylvia Rountree</b>, on-screen debut (in MA-005).",
 "<b>Silas Tillman</b> (b. September 2, 1920; WWII Okinawa veteran; 38 years with the Transit Authority) and <b>Corinthia Tillman</b> (b. May 15, 1923), married January 11, 1946; their daughter died in 1951. <b>Keisha Bowman</b> (b. October 9, 1967), a paralegal. <b>Rev. Dr. Elias Montgomery</b> (b. June 30, 1937)."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["On January 11, 2006, the Alito confirmation hearings were in their third day, Ariel Sharon had been comatose since his January 4 stroke, and the January 2 Sago Mine explosion had killed 12 miners (one survivor). USMLE scores are customarily released on Wednesdays. Widener Library is Harvard's main library. FEMA rental assistance housed many Katrina evacuees in New York.",
 "Medicine: AAA repair is indicated above 5.5 cm or when symptomatic. A ruptured AAA with a retroperitoneal hematoma can be temporized with supraceliac compression and repaired with a Dacron tube graft. Renal and cardiac complications are common in octogenarians. "
 "Exertional rhabdomyolysis from 'boot camp' spin classes causes myoglobinuric kidney injury and compartment syndrome; fasciotomy is indicated when the delta pressure (diastolic minus compartment) is under 30 mmHg. An 'electrical storm' is three or more VT/VF episodes in 24 hours (here two shocks within minutes), treated with amiodarone, lidocaine and electrolyte repletion. An LVAD can bridge a deteriorating 1A candidate to transplant."])
