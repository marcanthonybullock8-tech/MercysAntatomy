import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E11_If_You_Dont_Know_Me_by_Now.pdf')
PARTS = [D + 's2e11_part1.txt', D + 's2e11_part2.txt', D + 's2e11_part3.txt']
EP = date(2005, 12, 9)
CODE = '2x11'
SEASON_LINE = 'Season 2, Episode 11'
TITLE = "If You Don't Know Me by Now"
COUNTERPART = "Episode 2x11. The counterpart of <i>Grey's Anatomy</i> 2x11."
DATES = 'Friday, December 9, 2005 (first snowstorm of the winter), 5:18 AM through 11:57 PM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x10'
AGES_ON = 'Friday, December 9, 2005'

CAST = [
 ("Tanya Harrell (new)", "Patient: Rikers detainee, swallowed foreign bodies", date(1976,5,3)), ("Officer Annette Biggs", "NYC Corrections Officer; Jermaine's mother", date(1953,11,3)),
 ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)), ("Dr. Raven Ellison", "Surgical Intern (26 since December 3)", date(1979,12,3)),
 ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)), ("Dr. Amond Baker", "Surgical Intern", date(1979,2,10)),
 ("Dr. Arianna Cummings", "Surgical Intern (Step 2 CK retake Monday)", date(1979,10,25)), ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)),
 ("Raymond 'Big Ray' Toles", "Chief of Security", date(1960,1,1)), ("Dr. Elxa Bullock", "Surgical Resident (31 weeks pregnant)", date(1977,8,29)),
 ("Dr. Bryce Kennerly", "Surgical Intern (on probation)", date(1978,6,11)), ("Dr. Abraham Lowery", "Attending General Surgeon", date(1947,1,9)),
 ("Darius 'Dash' Duvall (debut)", "Patient: dilated cardiomyopathy, Status 1A", date(1971,8,8)), ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)),
 ("Tamika Wardell (new)", "Patient: quintuplets at 29w2d, abruption", date(1974,9,14)), ("Andre Wardell (new)", "Tamika's husband; accountant", date(1972,3,27)),
 ("Dr. Clayton Hartwell", "OB/GYN and Fetal Surgeon", date(1971,3,3)), ("Dr. Isaiah Crump", "Chief of Pediatric Surgery", date(1944,3,11)),
 ("Dr. Natasha Donohue", "Chief of Surgery", date(1958,6,2)), ("Dr. Horace Whitlow", "Chief of Medicine", date(1949,9,19)),
 ("Dr. Camille Toussaint", "Orthopedic Resident", date(1976,7,21)), ("Bernadette 'Bernie' Watkins", "Executive Assistant to the Chief", date(1950,6,6)),
 ("Lamont 'Monty' Gaines", "Owner, Monty's on Jackson", date(1962,10,10)), ("Lillian Divine", "Harmony's mother", date(1952,2,14)),
 ("Howard Divine", "Harmony's father", date(1950,8,30)), ("Jerome 'Jerry' and Ronald 'Ronnie' Divine", "Harmony's twin brothers", date(1972,5,5)),
 ("Mercy (new)", "A brindle pit bull puppy, about 10 weeks old", date(2005,9,30)),
]
ALSO = ("<i>Also appearing: a GI attending, a NICU attending, NICU nurses and fellows, an L&D nurse, a step-down night nurse, a snow-day wrist-fracture patient, and the Wardell quintuplets: "
        "Aaliyah (A), Andre Jr. (B), Brielle (C), Devin (D) and Elijah (E). Mentioned: Kiara Harrell (6), Corinne Smilley, Malcolm Sloan, Alicia Monroe and Big Ray's dog Biscuit.</i>")

MEDIA = [
 ("NEW YORK DAILY NEWS: \"LET IT SNOW!\"", "Friday, December 9, 2005",
  ["\"The first big snowstorm of the season blanketed the city today, snarling the morning commute and sending slips, falls and fender-benders into emergency rooms across the five boroughs...\""]),
 ("ASSOCIATED PRESS: \"JET SKIDS OFF SNOWY CHICAGO RUNWAY, KILLING BOY IN CAR\"", "Thursday, December 8, 2005",
  ["\"CHICAGO (AP) -- A Southwest Airlines jet landing in heavy snow at Midway Airport skidded off the runway, through a fence and into a street, striking cars and killing a 6-year-old boy...\" Also: federal air marshals shot and killed a passenger at Miami International Airport on Wednesday after he said he had a bomb; no bomb was found."]),
 ("QueensGraceConfidential (Blogger)", "Friday, December 9, 2005, 4:40 PM",
  ["<i>\"SNOW DAY AT THE GRACE. Five babies were born in OR 2 this morning, QUINTUPLETS, at 29 weeks. We're told the smallest didn't make it this afternoon, and we're not going to say anything else about that except that we're so sorry. "
   "In other news: an intern borrowed the lobby barber's clippers to give a transplant patient a line-up. Our source says he looks 'like a whole new man.' Also, we cannot confirm a puppy in the security office. We CAN confirm Bernie's shoe.\"</i> Comments (1,118)."]),
 ("Jamaica Hospital Medical Center: CT Chest Report (excerpt), patient Howard Divine", "Read Thursday, December 8, 2005",
  ["\"IMPRESSION: 6 mm solid noncalcified nodule, right upper lobe, smooth margins, unchanged in size compared with the chest radiograph of 9/6/2005. No mediastinal or hilar lymphadenopathy. RECOMMENDATION: Follow-up CT in 6 months.\""]),
 ("Medical recommendation, Dr. Amond Baker (cosigned by Dr. A. Lowery)", "Friday, December 9, 2005",
  ["\"Patient is POD 0 following small bowel resection for foreign-body perforation, with documented self-injury in punitive segregation. Medically recommend against return to punitive segregation. Recommend medical housing with mental health follow-up.\""]),
 ("SMS, Motorola RAZR (Raven Ellison to Arianna Cummings)", "Friday, December 9, 2005, 10:33 PM",
  ["<b>Raven:</b> \"k.\""]),
]

CONT = [p("Continuity Sheet: Episode 2x11", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>DASH DUVALL'S DEBUT</b> (34): idiopathic dilated cardiomyopathy, EF 15%, Status 1A since November 11, 2005, on continuous milrinone through a PICC, in Cardiac Step-Down Room 609. He owns two sneaker stores in Charlotte. He came to New York for a sneaker convention at the Javits Center in October, collapsed there, and 'never made it home.' <b>Raven gave him a line-up</b> with the lobby barber's clippers. Robert warned her: 'Be his doctor.' His pressure dropped to 86 and she paged Robert, but hesitated first. Dash: 'I'm working up to [asking you out].' This begins the R-5 storyline.",
 "<b>Arianna and Raven fought</b> over Dash: 'Why did it take you so long to pick up the phone?' Arianna's Step 2 CK retake is Monday, December 12. That night Raven texted 'k.' and Arianna almost smiled.",
 "<b>The Wardell quintuplets</b> were born at 29w2d by crash cesarean for abruption (Hartwell). Five neonatal teams worked them (Crump; Elxa with Arianna; two NICU fellows; Marc). <b>Marc intubated Baby E, Elijah (680 g)</b>, who had bilateral grade III/IV intraventricular hemorrhage. Marc told the parents himself. Elijah died in his mother's arms at 4:02 PM; Crump called it. <b>Four of five survive:</b> Aaliyah, Andre Jr., Brielle and Devin (gastroschisis, silo placed by Crump with Marc). Tamika had refused selective reduction at 12 weeks and blamed herself. Crump told Marc he wants someone 'who knows the mothers' to succeed him: 'Two more winters, maybe three.'",
 "<b>Tanya Harrell</b> (29) is a Rikers pretrial detainee held since April on a $1,500 bail she can't pay, for $400 of baby formula. She spent 210 days in punitive segregation ('the Bing') for breaking the nose of a woman who tore up her daughter Kiara's letters. She swallowed two AA batteries and a pen clip; one battery came out by endoscopy, and the pen clip perforated her ileum (resection by Lowery and Baker). <b>Amond went from 'I don't think about her' to writing a medical recommendation against segregation</b>, and she got 30 days of medical housing. Kennerly challenged him, and Lowery: 'Go find out why.'",
 "<b>MERCY THE DOG:</b> a brindle pit bull puppy (about 10 weeks old, one ear up, one down), found by <b>Marc and Esther together</b> in a box behind Monty's dumpster at 6:34 AM. Big Ray kept her under his desk all day. Bernie is smitten. She wears the red leather collar of Big Ray's late dog Biscuit (his daughter lives in Atlanta). Marc named her at Monty's. She lives at 49th Avenue, and Esther now has dog hair on her scarf. Clayton: 'We should get a dog. Someday.'",
 "<b>Howard Divine's CT</b> (read December 8): 6 mm solid RUL nodule, unchanged since September, no nodes; repeat CT in June 2006. 'My daddy's got a June.' <b>Harmony introduced Camille to her family as 'my girlfriend.'</b> Lillian: 'I know, Baby Girl.' Howard welcomed her. Ronnie: 'You hurt our sister, we break your femurs.' This is the opposite of Augustin's rejection.",
 "<b>Malcolm accepted Corinne's invitation</b> to Christmas Eve in Mattapan; he'll bring sweet potato pies from the Twelfth Baptist church ladies. Esther wants Clayton there: 'It's Mattapan, Clayton. It's both.'",
 "<b>Whitlow asked for Amond</b> to present the Tate case at Medicine Grand Rounds on December 20, ahead of the January 15 Evidence of Standards Compliance deadline. Amond agreed 'for Mr. Tate's daughter.' Officer Biggs thanked Amond 'for looking twice.' Her son Jermaine is recovering. Elxa told Marc about her first-year neonatal death (a 24-weeker, in an ambulance on the Van Wyck)."])
CONT.append(p("Knowledge Tracker (as of December 9, 2005)", H2))
CONT.append(tbl([["Item", "Who knows"],
 ["Raven's feelings for Dash", "Raven (denying), Dash, Robert (suspects), Arianna, Marc, the blog"],
 ["Mercy the dog", "The housemates, Esther, Clayton, Big Ray, Bernie, Monty; Natasha 'has not been told'"],
 ["Harmony and Camille", "The Divine family now knows; Augustin knows and rejects it"],
 ["Howard's nodule (stable)", "The Divines, Camille"],
 ["Heir designation", "Still secret"]],
 [2.6*inch, 3.8*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Tanya Harrell", "5/3/1976 (29)", "Ingested 2 AA batteries and a pen clip; ileal perforation", "EGD retrieval; small bowel resection (Lowery; Baker; Kennerly)", "Recovering; medical housing"],
 ["Tamika Wardell", "9/14/1974 (31)", "Quintuplets at 29w2d, placental abruption", "Crash cesarean (Hartwell)", "Stable"],
 ["Wardell A, B, C", "12/9/2005", "Prematurity (1,100 / 1,200 / 1,000 g)", "Resuscitation; CPAP (Crump; Elxa, Cummings)", "Stable in NICU"],
 ["Wardell D (Devin)", "12/9/2005", "Prematurity, 950 g; gastroschisis", "Silo placement (Crump; Bullock)", "Stable"],
 ["Wardell E (Elijah)", "12/9/2005", "Prematurity, 680 g; bilateral grade III/IV IVH", "Intubation and surfactant (Bullock); comfort care", "Died at 4:02 PM"],
 ["Darius 'Dash' Duvall", "8/8/1971 (34)", "Idiopathic DCM, EF 15%, Status 1A; hypotension to 86", "Milrinone increased (R. Bullock; Ellison)", "Recovered to 94 systolic; waiting for a heart"]],
 [1.1*inch, 0.85*inch, 1.75*inch, 1.75*inch, 0.95*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Darius 'Dash' Duvall</b> (b. August 8, 1971), debut (in MA-005). <b>Tanya Harrell</b> (b. May 3, 1976) and her daughter <b>Kiara</b> (6, mentioned). <b>Tamika Wardell</b> (b. September 14, 1974), a third-grade teacher, and <b>Andre Wardell</b> (b. March 27, 1972), an accountant, with their quintuplets, born December 9, 2005.",
 "<b>Mercy</b>, a pit bull puppy (estimated birth late September 2005). Jerry and Ronnie Divine appear on screen."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["The first significant snowstorm of the 2005-06 winter hit New York on Friday, December 9, 2005. On December 8, 2005, Southwest Airlines Flight 1248 overran a snowy runway at Chicago Midway and struck cars, killing a 6-year-old boy. On December 7, 2005, federal air marshals shot a passenger at Miami International Airport. "
 "Rikers Island's women's jail is the Rose M. Singer Center, and punitive segregation is known among detainees as 'the Bing.' Twelfth Baptist Church is in Roxbury.",
 "Medicine: most cylindrical batteries in the stomach pass or can be retrieved endoscopically, and sharp objects can perforate the bowel near the ileocecal valve. Higher-order multiples at 29 weeks need one resuscitation team per infant. Infants under 750 g have high rates of severe intraventricular hemorrhage, and grade IV IVH carries a grave prognosis. "
 "Gastroschisis is managed with a preformed silo and staged reduction. Status 1A heart transplant candidates are often inpatients on continuous inotropes such as milrinone."])
