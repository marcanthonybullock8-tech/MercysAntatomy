import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E19_Deserve.pdf')
PARTS = [D + 's2e19_part1.txt', D + 's2e19_part2.txt', D + 's2e19_part3.txt']
EP = date(2006, 2, 27)
CODE = '2x19'
SEASON_LINE = 'Season 2, Episode 19'
TITLE = 'Deserve'
COUNTERPART = "Episode 2x19. The counterpart of <i>Grey's Anatomy</i> 2x19."
DATES = 'Monday, February 27, 2006 (Lundi Gras), 6:08 AM through 11:58 PM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x18'
AGES_ON = 'Monday, February 27, 2006'

CAST = [
 ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)), ("Dr. Raven Ellison", "Surgical Intern", date(1979,12,3)),
 ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)), ("Dr. Faith Danforth (debut)", "Veterinarian, Astoria Animal Hospital", date(1972,11,2)),
 ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)), ("Dr. Amond Baker", "Surgical Intern", date(1979,2,10)),
 ("Dr. Arianna Cummings", "Surgical Intern", date(1979,10,25)), ("Dr. Nnamdi Okoye", "Surgical Resident (PGY-4)", date(1974,10,1)),
 ("Dr. Elxa Bullock", "Surgical Resident (on maternity leave)", date(1977,8,29)), ("Quinton Rhames (new)", "Patient: GSWs to the liver; homicide suspect", date(1981,6,30)),
 ("Dr. Abraham Lowery", "Attending General Surgeon", date(1947,1,9)), ("Nurse Gloria Pettiford", "Head ER Nurse", date(1952,4,14)),
 ("Darius 'Dash' Duvall", "Patient: LVAD driveline infection (readmitted)", date(1971,8,8)), ("Glenda Duvall", "Dash's mother", date(1947,12,12)),
 ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery (50 since February 10)", date(1956,2,10)), ("Dr. Clayton Hartwell", "OB/GYN and Fetal Surgeon (patient, discreetly)", date(1971,3,3)),
 ("Dr. Natasha Donohue", "Chief of Surgery", date(1958,6,2)), ("Bernadette 'Bernie' Watkins", "Executive Assistant to the Chief", date(1950,6,6)),
 ("Sister Khadijah Bey (new)", "Widow of Abdul-Rahman Bey", date(1947,9,1)), ("Yusuf Bey (new)", "Khadijah's son; Con Ed worker", date(1975,12,20)),
 ("Dr. Bryce Kennerly", "Surgical Intern", date(1978,6,11)), ("Lamont 'Monty' Gaines", "Owner, Monty's on Jackson", date(1962,10,10)),
 ("Nurse Kendra Wallace", "Surgical Floor Nurse", date(1980,5,30)), ("Dr. Malcolm Sloan", "Chief of Plastic Surgery", date(1968,2,14)),
 ("Dr. Camille Toussaint", "Orthopedic Resident", date(1976,7,21)), ("Russell Jeffries", "Elxa's husband", date(1975,4,3)),
 ("Dr. Leland Graves", "Chief of Neurosurgery", date(1953,4,18)), ("Dorothea Rhames (new)", "Quinton's mother; home-care aide", date(1961,8,8)),
 ("Dr. Harold Bynum", "Consult-Liaison Psychiatrist", date(1942,10,19)), ("Dr. Paulette Greenidge", "Couples therapist, Montague Street", date(1955,8,1)),
 ("Russell Harmon 'Tuck' Jeffries Jr.", "Elxa's son (3 weeks)", date(2006,2,5)), ("Mercy", "The House's pit bull puppy (5 months)", date(2005,9,30)),
]
ALSO = ("<i>Also appearing: paramedics, two NYPD officers, a homicide detective, an anesthesiologist, ICU nurses, a teenager with a wrist fracture, and a rescued kitten. "
        "Mentioned: Abdul-Rahman Bey (killed at 7:10 AM), Augustin Toussaint, Raymond Cummings, Kat Smilley and a Ditmars Labrador with a cake habit.</i>")

MEDIA = [
 ("NEW YORK DAILY NEWS: \"CORONA GROCER SLAIN IN HOLDUP; SUSPECT SHOT BY COPS\"", "Monday, February 27, 2006 (afternoon edition)",
  ["\"Abdul-Rahman Bey, 57, who had run Bey's Grocery on Roosevelt Avenue since 1972 and was known on the block for extending credit to struggling mothers, was shot dead this morning during a robbery. Police shot the 24-year-old suspect as he fled. He is in critical condition at Queens Grace Hospital.\" (A fictional event.)"]),
 ("ASSOCIATED PRESS: \"SHANI DAVIS MAKES OLYMPIC HISTORY\" / \"OCTAVIA BUTLER, SCI-FI PIONEER, DIES AT 58\"", "February 2006",
  ["\"TURIN, Italy (AP) -- Shani Davis of Chicago won the 1,000 meters on Feb. 18, becoming the first Black athlete to win an individual gold medal at the Winter Olympics...\" / \"SEATTLE (AP) -- Octavia E. Butler, the award-winning science fiction author of 'Kindred' and 'Parable of the Sower,' died Feb. 24 at 58.\" (The Turin Games closed February 26.)"]),
 ("QueensGraceConfidential (Blogger)", "Monday, February 27, 2006, 7:44 PM",
  ["<i>\"A WIDOW IN THE SICU. We'll keep this short and respectful. A woman whose husband was killed this morning on Roosevelt Avenue walked into the room of the man accused of killing him, said her piece, and walked out. That's all. We can't stop thinking about it. "
   "Lighter notes: a certain Chief of OB was spotted walking VERY carefully today and refusing to sit. A certain intern from the 49th Avenue house has a DATE on Saturday with a VET who rides a VESPA. And a certain transplant patient on his second LVAD admission met a certain girlfriend and they shook hands. Stay tuned.\"</i> Comments (3,377)."]),
 ("Card with a Valentine's box (chewed): Dash Duvall to Raven Ellison", "Delivered February 24, 2006",
  ["\"To my Valentine. Sorry it's late. They don't let you buy candy in the CVICU. -D.\""]),
 ("Note left in Clayton Hartwell's mailbox", "Sunday, February 26, 2006",
  ["\"Lunch. Monty's. Any day. You pick. -M.\""]),
 ("Window sign, Bey's Grocery, Roosevelt Avenue", "Hand-lettered, about 1990",
  ["\"BEY'S GROCERY -- SINCE 1972 -- CREDIT FOR MOTHERS\""]),
]

CONT = [p("Continuity Sheet: Episode 2x19", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>DR. FAITH DANFORTH'S DEBUT</b> (33; counterpart of Finn Dandridge): Astoria Animal Hospital on 31st Street under the N train (est. 1962). She lives upstairs, rides a red Vespa over the Pulaski Bridge, and has a UConn veterinary background. <b>Mercy ate twelve Godiva dark-chocolate truffles</b> (Dash's late Valentine to Raven) at about 5:50 AM. Faith opened at 6:31 AM in pajamas and treated theobromine toxicity with apomorphine, activated charcoal, IV fluids and cardiac monitoring (HR 190, down to 96). She recognized Marc from the news and said nothing: 'I read the vet journals and the comics.' <b>She asked Marc to dinner Saturday, March 4, at Taverna Kyclades on Ditmars</b> ('Dogs are complicated. I'm not'), and he said yes. She sent Mercy home with a chocolate-bar chew toy. The bill was $212.",
 "<b>Esther is jealous of Faith</b> (Amond: 'That was jealousy, Marc'). Malcolm read it on her face ('the face you made when your sister Kat got the bigger bike'). <b>Esther told Clayton</b> under No More Octobers: 'I was jealous anyway. That's the truth.' Clayton: 'It makes me sad. And grateful.' <b>Malcolm asked Clayton to lunch</b> by note ('Monty's. Any day. You pick'), and Esther told Malcolm to tell Clayton to go.",
 "<b>CLAYTON'S EMBARRASSING AILMENT</b> (counterpart of Addison asking Bailey): a golf-ball-sized perianal abscess for five days (he did a twin-twin laser standing on one leg). <b>Elxa, on maternity leave, drained it</b> in locked Procedure Room 2 with Tuck in the room: 'I'll drain your butt. But I'm bringing the baby.' Sitz baths, packing, and no sitting until Thursday. He told Esther, and she laughed until she had to sit down.",
 "<b>DASH READMITTED</b> (counterpart of Denny's readmission): the HeartMate went in February 14 (Raven second-assisted, Arianna watched from the gallery). He was discharged February 24 to Glenda's sublet on 21st Street, Astoria, walked to Steinway Street, and called it the best three days of his life. He was readmitted February 27 with an <b>MSSA driveline exit-site infection</b> (fever 102.8, pump pocket clear on ultrasound), on vancomycin/cefepime then six weeks of antibiotics, inpatient until a heart comes, still Status 1A. Raven: 'We're not over' (about Arianna). <b>Arianna and Dash met:</b> 'You're Problem.' 'You're the cantaloupe.' 'We're both in love with the same woman... Nobody in this room is lying.' 'I want you to get a heart, Duvall. So this is a fair fight.'",
 "<b>THE COUNSELING ARC:</b> Natasha and Robert's first session with <b>Dr. Paulette Greenidge</b> (Mondays, 'not Thursdays'). Robert: he kept the affair secret because Natasha was drinking (1985-86), then because of her sobriety, 'protecting myself.' Natasha: 'find out if a marriage can survive both of us having been the person who needed forgiving.' <b>Robert slept in their bedroom again</b>, on his side, on top of the covers. Both had been sleeping on office sofas some nights; Robert had 11 office nights in February (per Big Ray, Monty and Amond). Natasha told Elxa that her father 'did something a long time ago... before Grace was a year old,' but not what. <b>Marc's session 3 with Dr. Bynum:</b> 'Like holding the shell. Perfectly still on the outside. And inside, everything white.' Faith 'wasn't white.'",
 "<b>The Bey case:</b> Quinton Rhames (24, of the Lefrak City towers) shot and killed grocer <b>Abdul-Rahman Bey</b> (57) at 7:10 AM on Roosevelt Avenue for $180 and two cartons of Newports, and was shot by police. Lowery and Marc did a Pringle maneuver and damage-control liver packing (relook Wednesday). He wrote 'IS HE DEAD' and 'I DIDNT MEAN TO. GUN WENT OFF.' <b>Marc gave the clipboard to the officer.</b> <b>Sister Khadijah Bey</b> came to his bedside: 'I'm not here to forgive you... My husband would have handed you a broom.' That night she swept the store floor, and it opens at 6 AM. Arianna sat with Quinton's mother Dorothea, and Natasha approved her visit.",
 "<b>Arianna's past (new canon):</b> her father Raymond Cummings shot a man over $40 of heroin in 1996 (the man lived) and did six years at Western Penitentiary, Pittsburgh. The victim's daughter was in her class at Schenley High School. <b>Kennerly asked Kendra to dinner Friday</b> ('Tablecloths. You're paying'). <b>Harmony and Camille at Augustin's on Sunday, February 26:</b> he shook Harmony's hand: 'Welcome, Harmony.' He made red beans and rice on a Sunday, breaking the Monday rule. <b>Mardi Gras dinner at Halsey Street is February 28:</b> 'Mardi Gras is the day you say what you are.' Camille bought the second King cake. Russell's cranioplasty is set for March 20, then teaching after Easter; his step team competes at Medgar Evers in April."])
CONT.append(p("Knowledge Tracker (as of February 27, 2006)", H2))
CONT.append(tbl([["Item", "Who knows"],
 ["Marc's Saturday date with Faith", "The housemates, Camille, Esther (by inference), the blog"],
 ["Clayton's abscess", "Elxa, Clayton, Esther (and the blog, vaguely)"],
 ["Natasha and Robert in counseling", "Bernie, Amond, Elxa (partial), Dr. Greenidge"],
 ["Robert's affair (content)", "Robert, Natasha, Dr. Greenidge; Amond (inferred); Elxa knows only 'something'"],
 ["Mariah Pettaway; the sealed letter", "No one / unopened"]],
 [2.6*inch, 3.8*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Quinton Rhames", "6/30/1981 (24)", "Two GSWs to the right upper quadrant; grade IV liver injury, retrohepatic bleeding", "Pringle; damage-control packing; temporary closure (Lowery; Bullock; Cummings)", "SICU under police guard; relook Wednesday"],
 ["Darius 'Dash' Duvall", "8/8/1971 (34)", "LVAD driveline infection (MSSA)", "Vancomycin/cefepime, then 6 weeks (R. Bullock; Baker; Ellison)", "Fever 100.4; inpatient until transplant"],
 ["Dr. Clayton Hartwell", "3/3/1971 (34)", "Perianal abscess", "Incision and drainage under local (E. Bullock)", "Sitz baths; no sitting until Thursday"],
 ["Mercy (canine)", "about 9/2005", "Theobromine toxicity (12 dark truffles)", "Apomorphine, activated charcoal, IV fluids (Danforth)", "Recovered"]],
 [1.1*inch, 0.85*inch, 1.75*inch, 1.75*inch, 0.95*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Dr. Faith Danforth</b>, debut (in MA-005). <b>Quinton Rhames</b> (b. June 30, 1981) and <b>Dorothea Rhames</b> (b. August 8, 1961). <b>Sister Khadijah Bey</b> (b. September 1, 1947) and <b>Yusuf Bey</b> (b. December 20, 1975); <b>Abdul-Rahman Bey</b> (1948-2006), mentioned."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["Shani Davis won the 1,000 m speed skating gold at the Turin Winter Olympics on February 18, 2006, the first Black athlete to win an individual Winter Olympic gold, and the Games closed February 26. Octavia E. Butler died February 24, 2006. February 27, 2006 was Lundi Gras and February 28 was Mardi Gras. Red beans and rice is traditionally a Monday dish in New Orleans.",
 "Medicine: theobromine toxicity in dogs is dose-dependent and worst with dark chocolate. It is treated with induced emesis (apomorphine) within a few hours, activated charcoal, fluids and cardiac monitoring. Driveline infection is the most common complication of a pulsatile LVAD, and device complications qualified candidates for Status 1A. "
 "Damage-control laparotomy (perihepatic packing, temporary closure, ICU resuscitation, relook in 24-72 hours) is standard for exsanguinating liver injury, and the Pringle maneuver occludes the portal triad. Perianal abscesses need incision and drainage, followed by sitz baths."])
