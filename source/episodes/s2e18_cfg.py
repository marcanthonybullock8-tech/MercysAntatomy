import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E18_Back_in_the_Day.pdf')
PARTS = [D + 's2e18_part1.txt', D + 's2e18_part2.txt', D + 's2e18_part3.txt']
EP = date(2006, 2, 13)
CODE = '2x18'
SEASON_LINE = 'Season 2, Episode 18'
TITLE = 'Back in the Day'
COUNTERPART = "Episode 2x18. The counterpart of <i>Grey's Anatomy</i> 2x18 (the Sloan arrival and the flashback episode)."
DATES = 'Monday, February 13, 2006 (the morning after the Blizzard of 2006), 6:11 AM through 11:58 PM, with flashbacks to March 10-11, 1990'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x17'
AGES_ON = 'Monday, February 13, 2006 (flashback ages are given in the scene action)'

CAST = [
 ("Dr. Natasha Donohue", "Chief of Surgery (also seen at 31, in 1990)", date(1958,6,2)),
 ("Dr. Malcolm Sloan (on-screen debut)", "Chief of Plastic and Reconstructive Surgery (first day)", date(1968,2,14)), ("Raymond 'Big Ray' Toles", "Chief of Security", date(1960,1,1)),
 ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)), ("Dr. Raven Ellison", "Surgical Intern", date(1979,12,3)),
 ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)), ("Dr. Amond Baker", "Surgical Intern (27 since February 10)", date(1979,2,10)),
 ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)), ("Dr. Arianna Cummings", "Surgical Intern", date(1979,10,25)),
 ("Dr. Bryce Kennerly", "Surgical Intern", date(1978,6,11)), ("Nurse Kendra Wallace", "Surgical Floor Nurse", date(1980,5,30)),
 ("Dr. Nnamdi Okoye (new)", "Surgical Resident (PGY-4), covering Elxa's leave", date(1974,10,1)), ("Nurse Gloria Pettiford", "Head ER Nurse", date(1952,4,14)),
 ("Gunnery Sgt. Ezekiel Holcomb, USMC (Ret.) (new)", "Patient: severe accidental hypothermia, cardiac arrest", date(1951,7,4)), ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)),
 ("Bernadette 'Bernie' Watkins", "Executive Assistant to the Chief", date(1950,6,6)), ("Dr. Clayton Hartwell", "OB/GYN and Fetal Surgeon", date(1971,3,3)),
 ("Zaria Holmes (new)", "Patient, 7: dog bite, facial avulsion, depressed skull fracture", date(1998,9,3)), ("Trina Holmes (new)", "Zaria's mother", date(1976,12,15)),
 ("Dr. Abraham Lowery", "Attending General Surgeon", date(1947,1,9)), ("Russell Jeffries", "Elxa's husband (post-craniectomy)", date(1975,4,3)),
 ("Dr. Elxa Bullock", "Surgical Resident (maternity leave)", date(1977,8,29)), ("Dr. Joan Mercer (flashback)", "Marc's grandmother, at 54 in 1990", date(1935,4,17)),
 ("Dr. Victor Donohue (flashback)", "Marc's grandfather, at 56 in 1990", date(1933,5,30)), ("Dr. Leland Graves", "Chief of Neurosurgery", date(1953,4,18)),
 ("Darius 'Dash' Duvall", "Patient: Status 1A, day 94; LVAD consented", date(1971,8,8)), ("Glenda Duvall", "Dash's mother", date(1947,12,12)),
 ("Dr. Camille Toussaint", "Orthopedic Resident", date(1976,7,21)), ("Augustin Toussaint (V.O.)", "Camille's father", date(1941,2,9)),
 ("Dr. Harold Bynum", "Consult-Liaison Psychiatrist", date(1942,10,19)), ("Lamont 'Monty' Gaines", "Owner, Monty's on Jackson", date(1962,10,10)),
 ("Russell Harmon 'Tuck' Jeffries Jr.", "Elxa's son (8 days old)", date(2006,2,5)), ("Mercy", "The House's pit bull puppy", date(2005,9,30)),
]
ALSO = ("<i>Also appearing (flashback): Young Marc, age 11, in March 1990. Also appearing: a hospital volunteer, a perfusionist, paramedics, the meeting chairpersons and members at Saint Paul's (1990) and St. Mary's (2006), and a plow driver. "
        "Mentioned: Imani and Angela Burrell, Sgt. Isaac Burrell (funeral, Friday, February 10, Greater Allen Cathedral), Corinne Smilley, Dr. Delphine Ware, Alphonse, Mr. Duvall Sr. (d. June 9, 1990) and Celia Montague.</i>")

MEDIA = [
 ("THE NEW YORK TIMES: \"RECORD SNOW BURIES CITY\"", "Monday, February 13, 2006",
  ["\"A blizzard dropped 26.9 inches of snow on Central Park on Saturday and Sunday, the most since record-keeping began in 1869, shutting the airports and stranding travelers... Sanitation crews worked through the night...\""]),
 ("ASSOCIATED PRESS: \"CHENEY ACCIDENTALLY SHOOTS FELLOW HUNTER\"", "Monday, February 13, 2006",
  ["\"WASHINGTON (AP) -- Vice President Dick Cheney accidentally shot and wounded a companion, Harry Whittington, during a quail hunt on a Texas ranch on Saturday. The incident was not disclosed until Sunday...\""]),
 ("QueensGraceConfidential (Blogger)", "Monday, February 13, 2006, 8:22 AM",
  ["<i>\"DAY ONE, ROUND ONE. The new Chief of Plastics arrived at 7:02 AM looking like a cologne ad, asked for the EAST STAIRS (?!), and by 7:41 had a broken nose courtesy of a certain intern from Boston with a right cross we can only call 'Mattapan.' "
   "He says he walked into a door. We have three witnesses who say the door was 5'6\" and wearing scrubs. Also: a frozen Marine came back to life on bypass in Trauma 2 after 70 minutes. Not dead until warm and dead, people.\"</i> Comments (5,118)."]),
 ("Card tucked into a King cake (Augustin Toussaint to Harmony Divine)", "Delivered Monday, February 13, 2006",
  ["\"Dr. Divine. It is the season of Carnival. In New Orleans we eat this from Twelfth Night until Mardi Gras. Whoever finds the baby in her slice must buy the next cake. I am told you are very good with babies. A. Toussaint.\""]),
 ("Card inside a pink T-Mobile Sidekick (Marc Bullock to Imani Burrell)", "Given at the repast, Friday, February 10, 2006",
  ["\"From your daddy. He said yes.\""]),
 ("Sign beneath a newspaper photo, Surgical Floor nurses' station", "Posted February 2006",
  ["\"SGT. ISAAC BURRELL. 1961-2006. HE WALKED IT OUT.\""]),
]

CONT = [p("Continuity Sheet: Episode 2x18", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>MALCOLM SLOAN'S ON-SCREEN DEBUT</b> (37; 38 on February 14): Chief of Plastic and Reconstructive Surgery, first day February 13, 2006. He arrived at 7:02 AM and took the east stairs. <b>Esther punched him</b> (a right cross; Clarence Smilley taught all five daughters boxing in the back of Smilley's Hardware) in the Plastics corridor at 7:38 AM: 'That's for the stairs... I don't want you hiding from me.' This is the counterpart of Derek punching Mark. He set his own nose, has two black eyes, and told everyone he 'walked into a door.' Natasha did not read the three witness statements. <b>He used the elevator; Esther rode seven floors with him</b> ('It's just the elevator'). Esther told Clayton: 'His hands are still the best hands I've ever seen.'",
 "<b>Clayton and Malcolm</b> met for the first time since Back Bay in February 2005. Clayton: 'I'm her husband. I'm staying her husband.' Malcolm: 'I came for her... For Ma Corinne's table.' <b>Malcolm and Marc</b> met at Monty's: 'She looked down the hall toward the elevators... I'm not the one she was looking for anymore.' Malcolm and Esther operated together on Zaria Holmes (72 stitches). Esther held the nails for Malcolm when she was six, while he fixed bikes in the store.",
 "<b>ROBERT'S CONFESSION</b> (11:52 AM, Chief's office): a two-month affair with <b>Dr. Delphine Ware</b> (then a 4th-year Howard surgery resident) in <b>October and November 1981</b>, beginning at a surgical meeting in Chicago, her hometown. Robert was a third-year medical student. It ended before Christmas, and she returned to Chicago in spring 1982. <b>Grace was six months old</b>, and Natasha was a second-year HMS student in Cambridge. Robert revealed the sealed letter in the glove compartment, unopened. <b>Natasha: 'Don't open it. Not until we're both ready to know.'</b> She is not leaving and not forgiving, and is 'sleeping in Grace's room.' <b>Mariah's existence is still unknown to everyone</b> (S11 payoff).",
 "<b>THE 1990 FLASHBACKS</b> (counterpart of the Ellis flashbacks): Saturday, March 10, 1990, 11:41 PM, at the Brookline apartment, <b>Marc (11) put out a stove fire with an extinguisher</b> while Natasha (31) was passed out drunk at the kitchen table. Robert was in Baltimore (Hopkins). On March 11, <b>Joan Mercer</b> took Natasha to her first AA meeting at Saint Paul's in Brookline ('You come from women who do hard things in front of people who are watching'), and Victor took Marc for pancakes. <b>Robert drove seven hours overnight from Baltimore</b> and sat in the last chair. <b>Natasha's sobriety date is March 11, 1990</b> (15 years, 11 months). Marc checks the stove knobs twice, a habit since 1990; tonight he checked once.",
 "<b>Natasha shared at an AA meeting</b> in St. Mary's basement on Vernon Boulevard (Mondays, 3 PM). <b>Bernie Watkins has 22 years of sobriety</b> (Mondays and Tuesdays) and never told Natasha. <b>Marc started therapy with Dr. Harold Bynum</b> (Amond made the appointment from Lowery's phone), Mondays at 4 PM, for post-blast startle and dissociation. He told Bynum about the fire for the first time in 16 years: 'A bomb is just one more thing on the stove.' <b>Lowery's backstory:</b> Navy corpsman with Marines near Da Nang in 1967, then postwar startle on Fulton Street in Bed-Stuy, then the VA in 1968, then medical school on the G.I. Bill.",
 "<b>Dash consented to a HeartMate bridge LVAD</b> for February 14 at 7 AM (creatinine 2.4, rising LFTs; day 94). Glenda told him his father died June 9, 1990, refusing 'a machine.' Robert: Amond first-assists and <b>Raven second-assists</b> ('She'll hold a retractor. Not his hand'). Dash: 'You're my Valentine. Don't argue.' Arianna will watch from the gallery 'for you.' <b>Arianna came back to 49th Avenue for dinner</b>, the first time since January 20.",
 "<b>Augustin sent Harmony a King cake</b> addressed to 'Dr. Divine' (he drove to the Louisiana bakery on Fulton Street in the snow, and he fears snow). By phone: 'Forgiving people and not telling them... a bad habit of mine.' <b>Camille found the baby</b>, so she buys the next cake and will take Harmony to Halsey Street. <b>Gunny Ezekiel Holcomb</b> (54, Beirut 1983), found in a snowbank under the Pulaski Bridge with a core temperature of 24.1 C, survived 70 minutes of arrest via bypass rewarming (Kennerly, Arianna, R. Bullock, Baker). Celia got him a bed at the Bronx VA. 'Semper fi, Doc.' <b>Burrell's funeral</b> was Friday, February 10, at Greater Allen Cathedral. Marc gave Imani a pink Sidekick: 'From your daddy. He said yes.' <b>Dr. Nnamdi Okoye</b> (PGY-4) runs the board during Elxa's leave (to April); Elxa left eleven pages, ending with 'Watch Bullock.' Russell is extubated and wears a helmet until the bone flap goes back in about six weeks."])
CONT.append(p("Knowledge Tracker (as of February 13, 2006)", H2))
CONT.append(tbl([["Item", "Who knows"],
 ["Robert's 1981 affair with Delphine Ware", "Robert, Natasha; Amond (inferred from Langley); Bernie (from the share, without names)"],
 ["The 1990 fire and Natasha's drinking", "Natasha, Robert, Victor, Joan, Elxa, Grace (as children); now Dr. Bynum and the St. Mary's group"],
 ["Bernie is in recovery", "Natasha"],
 ["Mariah Pettaway", "No one. Locked until Season 11"],
 ["Heir designation", "Still secret (Victor wants to move it up)"]],
 [2.6*inch, 3.8*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Gunny Ezekiel Holcomb", "7/4/1951 (54)", "Severe hypothermia (24.1 C), VF arrest for 70 minutes", "CPR; warm irrigation; femoral bypass rewarming; defibrillation at 30 C (Kennerly; Cummings; R. Bullock; Baker)", "ROSC; extubated; frostbite to two fingertips"],
 ["Zaria Holmes", "9/3/1998 (7)", "Dog bite: left forehead and temporal avulsion, depressed skull fracture", "Elevation and dural repair (Graves; Smilley); flap replacement, 72 sutures (Sloan; Smilley; Bullock)", "Neurologically intact"],
 ["Darius 'Dash' Duvall", "8/8/1971 (34)", "DCM, worsening renal and hepatic function, day 94", "LVAD consented for February 14 (R. Bullock; Baker; Ellison)", "Pending"],
 ["Russell Jeffries", "4/3/1975 (30)", "Post-craniectomy", "Extubated; helmet", "Recovering"]],
 [1.1*inch, 0.85*inch, 1.75*inch, 1.75*inch, 0.95*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Dr. Malcolm Sloan</b>, on-screen debut (in MA-005). <b>Dr. Nnamdi Okoye</b> (b. October 1, 1974), PGY-4. <b>Gunnery Sgt. Ezekiel Holcomb</b> (b. July 4, 1951). <b>Zaria Holmes</b> (b. September 3, 1998) and <b>Trina Holmes</b> (b. December 15, 1976).",
 "<b>Dr. Joan Mercer</b> and <b>Victor Donohue</b> appear in flashback, with <b>Young Marc</b> (11) and <b>Natasha</b> (31)."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["The Blizzard of February 11-12, 2006 dropped 26.9 inches on Central Park, then the city's largest snowfall since record-keeping began in 1869. Vice President Cheney accidentally shot Harry Whittington on February 11, 2006, and it was disclosed the next day. Greater Allen A.M.E. Cathedral in Jamaica hosts large funerals. The James J. Peters VA Medical Center is in the Bronx.",
 "Medicine: in severe accidental hypothermia, 'nobody is dead until warm and dead.' Extracorporeal rewarming (cardiopulmonary bypass or ECMO) can produce good neurologic survival after prolonged CPR, and defibrillation is often deferred until core temperature reaches about 30 C. "
 "Dog-bite facial avulsions are irrigated, debrided and replaced anatomically, often with excellent cosmetic results in children, and a depressed skull fracture with dural tear needs elevation and repair. Rabies observation of the biting dog is standard. A bridge LVAD is indicated when inotrope-dependent heart failure causes worsening end-organ (renal, hepatic) function. Startle, dissociation and hypervigilance after a blast are common acute stress responses, and early counseling helps."])
