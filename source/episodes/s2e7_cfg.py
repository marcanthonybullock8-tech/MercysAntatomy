import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E07_Something_to_Talk_About.pdf')
PARTS = [D + 's2e7_part1.txt', D + 's2e7_part2.txt', D + 's2e7_part3.txt']
EP = date(2005, 11, 4)
CODE = '2x07'
SEASON_LINE = 'Season 2, Episode 7'
TITLE = 'Something to Talk About'
COUNTERPART = "Episode 2x07. The counterpart of <i>Grey's Anatomy</i> 2x07."
DATES = 'Friday, November 4, 2005, 5:51 AM through 11:56 PM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x06'
AGES_ON = 'Friday, November 4, 2005'

CAST = [
 ("Dr. Bryce Kennerly", "Surgical Intern (on probation)", date(1978,6,11)), ("Nurse Kendra Wallace", "Surgical Floor Nurse", date(1980,5,30)),
 ("Dr. Philip Grant (new)", "Medicine Resident", date(1976,3,13)), ("Josephine 'Grandma Jo' Bullock (on-screen debut)", "Marc's paternal grandmother", date(1931,1,19)),
 ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)), ("Dr. Raven Ellison", "Surgical Intern", date(1979,12,3)),
 ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)), ("Dr. Amond Baker", "Surgical Intern (back from leave)", date(1979,2,10)),
 ("Dr. Arianna Cummings", "Surgical Intern (26 since Oct 25)", date(1979,10,25)), ("Dr. Elxa Bullock", "Surgical Resident (26 weeks pregnant)", date(1977,8,29)),
 ("Dr. Isaiah Crump", "Chief of Pediatric Surgery", date(1944,3,11)), ("Dr. Clayton Hartwell", "Fetal Surgeon", date(1971,3,3)),
 ("Bernard 'Bunny' Washington (new)", "Patient: fetus in fetu", date(1973,4,19)), ("Bernadette 'Bernie' Watkins", "Executive Assistant to the Chief", date(1950,6,6)),
 ("Dr. Natasha Donohue", "Chief of Surgery", date(1958,6,2)), ("Franklin Bassett, Esq.", "General Counsel", date(1958,10,28)),
 ("Nadia Ellerbe", "Patient: chorioamnionitis, cesarean at 30w6d", date(1977,4,25)), ("Malik Ellerbe", "Nadia's husband", date(1975,1,30)),
 ("Raymond 'Big Ray' Toles", "Chief of Security", date(1960,1,1)), ("Dr. Abraham Lowery", "Attending General Surgeon", date(1947,1,9)),
 ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)), ("Nurse Gloria Pettiford", "Head ER Nurse", date(1952,4,14)),
 ("Dr. Camille Toussaint", "Orthopedic Resident", date(1976,7,21)), ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)),
 ("Dr. Leland Graves", "Chief of Neurosurgery", date(1953,4,18)), ("Eddie (new)", "Monty's regular", date(1965,8,8)),
 ("Lamont 'Monty' Gaines", "Owner, Monty's on Jackson", date(1962,10,10)), ("Dr. Horace Whitlow", "Chief of Medicine", date(1949,9,19)),
 ("Dr. Grace Bullock (V.O.)", "Harvard Medical School student; Marc's sister", date(1981,4,12)), ("Dr. Victor Donohue (V.O.)", "Marc's grandfather", date(1933,5,30)),
]
ALSO = ("<i>Also appearing: Miss Hattie Lomax, two floor nurses, an L&D nurse, a NICU team, a circulating nurse, a lobby volunteer and Malik Ellerbe Jr. (born today, 3 lb 2 oz). "
        "Mentioned: Rosa Parks, Malcolm Sloan, Corinne Smilley, Augustin Toussaint, Tyrell Pickens (by postcard), Walter Bullock and Bunny's late mother.</i>")

MEDIA = [
 ("THE NEW YORK TIMES: \"ROSA PARKS IS LAID TO REST IN DETROIT\"", "Thursday, November 3, 2005",
  ["\"DETROIT -- Rosa Parks was buried Wednesday after a seven-hour funeral... Her body had lain in honor in the Capitol Rotunda in Washington on Sunday and Monday, the first woman so honored, as tens of thousands waited in line in the cold...\""]),
 ("ASSOCIATED PRESS: \"PROTESTS GREET BUSH AT SUMMIT IN ARGENTINA\" / \"RIOTS SPREAD IN PARIS SUBURBS\"", "Friday, November 4, 2005",
  ["\"MAR DEL PLATA, Argentina (AP) -- Thousands of protesters marched against President Bush as the Summit of the Americas opened...\" / \"PARIS (AP) -- Rioting spread for an eighth night across the suburbs of Paris...\""]),
 ("QueensGraceConfidential (Blogger)", "Friday, November 4, 2005, 4:02 PM",
  ["<i>\"IS DR. X THE CHIEF'S SON? We have held this story since July out of respect. Today it walked into our lobby in a church hat and called him 'baby' loud enough to be heard in Radiology. "
   "So: Dr. X is apparently Dr. Natasha Donohue's son, Dr. Elxa Bullock's brother, and (sit down) VICTOR DONOHUE's GRANDSON. Living in Hunters Point. With roommates. Taking the 7. "
   "We'll say what everybody in this building is saying: nobody can point to one thing he's gotten that he didn't earn. Also, a man had his TWIN removed from his abdomen today. Something to talk about indeed.\"</i> Comments (1,442)."]),
 ("Postcard: Tyrell Pickens to Dr. Elxa Bullock", "Postmarked Rocky Mount, N.C., October 31, 2005",
  ["\"Dr. Bullock. I start school Monday. Grandma made me wear the orange sweater. I look like a traffic cone. I'm alive. Thank you. -Tyrell P. (Bird)\""]),
 ("SMS, Motorola RAZR (Raven Ellison to Harmony Divine)", "Friday, November 4, 2005, 8:10 AM",
  ["<b>Raven:</b> \"its everywhere. chiefs son. elxas brother. donohue.\"", "<b>Harmony:</b> \"stairwell B. now.\""]),
 ("Whitlow's legal pad (top sheet)", "Friday, November 4, 2005, 10:38 PM",
  ["\"JOINT COMMISSION -- ANONYMOUS -- CONFLICT OF INTEREST / RESIDENT SUPERVISION.\" (underlined twice)"]),
]

CONT = [p("Continuity Sheet: Episode 2x07", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>The rumor:</b> at 5:51 AM, November 4, 2005, Kennerly told Kendra Wallace and Dr. Philip Grant in the cafeteria that Marc is the Chief's son and Victor's grandson, 'from a board member.' By noon it had reached the pharmacy, respiratory therapy and every nurses' station. Whitlow did not sign the board NDA (department chiefs weren't asked), so he is legally clear and deniable. Natasha: 'You disclosed to the cafeteria to destroy it.' Whitlow: 'I just had to make them wonder.' <b>Whitlow is now drafting an anonymous Joint Commission complaint</b> (conflict of interest and resident supervision).",
 "<b>Grandma Jo Bullock's on-screen debut</b> (74; retired fourth-grade teacher at Garnet-Patterson in Shaw for 31 years). She came from D.C. after Rosa Parks lay in honor (she waited four hours outside the Rotunda on Sunday, October 30). <b>She confirmed the rumor in the lobby</b> ('MARC-ANTHONY! Come give your grandmother some sugar!'), and Whitlow watched from the mezzanine. 'Lies are always on sale.' Walter Bullock drove the 70 bus up Georgia Avenue. Natasha sent Big Ray to Penn Station. Grandma Jo predicts Elxa's baby is a boy (Tuck is). Gloria and Grandma Jo met.",
 "<b>MARC TOLD RAVEN AND HARMONY</b> at dinner (7:31 PM, after Grandma Jo's pork chops): Natasha and Robert are his parents, Elxa and Grace his sisters, and Victor his grandfather. Victor was the one at the loading dock and in the Mercedes, and the house is Victor's. Raven: 'I knew it. I didn't know it, but I knew it.' Harmony: 'Five months... I found out from an elevator.' Marc: 'Because you were the one person in my life who liked me before you knew.' Harmony walked out (to Camille at Gantry pier), came back at 11:41 PM and said: 'I'm not going anywhere.' <b>The heir designation was not revealed.</b>",
 "<b>Raven learned Arianna had known since August 9</b>, and the two made up. <b>Raven's secret</b> (told only to Arianna, who keeps it even from Marc): her mother is alive, three years clean, in an apartment on MLK Boulevard in Savannah, and has written monthly. Raven has 34 unopened letters in a shoebox under her bed.",
 "<b>Esther and Clayton:</b> Malcolm Sloan called Clayton at 11:15 PM on November 3 about a possible NYU plastic surgery job. Clayton disclosed it the same day, and at Esther's request told Malcolm no ('not yet, maybe not ever'). Malcolm: 'Tell her I'll wait.' He has eaten Sunday dinner at the Smilleys' since 1978. <b>Esther brought her first box from the Clarence</b> to the Remsen Street sublet: 'It's not moving in. It's one box.'",
 "<b>Malik Ellerbe Jr.</b> was born by cesarean at 30w6d for chorioamnionitis, 3 lb 2 oz, Apgars 5 and 8, with a healed sacrococcygeal scar from fetal surgery. Christening at Bethel in January; Marc and Clayton are invited. Clayton: 'First open fetal I've done that I got to meet.'",
 "<b>Bunny Washington</b> had an 18 cm fetus in fetu resected (Crump; Clayton; Marc), with vertebrae, limb buds, two teeth and curly hair. It will be buried with his mother (d. 2002) at Woodlawn under the name 'Benny.'",
 "<b>Graves warned Kennerly</b>: 'Truth is not a defense for cruelty.' Graves's office holds a photo of him as a Mercer Scholar with Victor. <b>Lowery</b> called Raven and Arianna's quarrel a 'lovers' quarrel,' so he knows. Monty: 'I'm a vault with a tap.' Kendra apologized to Marc.",
 "<b>Victor will come to Thanksgiving at 49th Avenue</b> (November 24) 'with a pie in my hands' (he won't bake it). Grace called Marc: 'Tell them I'm the good Bullock.'"])
CONT.append(p("Knowledge Tracker (as of November 4, 2005)", H2))
CONT.append(tbl([["Group", "Knows Marc is Natasha and Robert's son and Victor's grandson?"],
 ["<b>Raven, Harmony</b>", "Yes, told by Marc at 7:31 PM"],
 ["QGH staff at large", "Rumor confirmed in practice by the blog and the lobby; not officially announced"],
 ["Board (8), Bassett, Whitlow, Lowery, Kennerly", "Yes"],
 ["Clayton", "Now effectively yes (everyone knows)"],
 ["Heir designation (2001 will and sealed letter)", "Still secret: Victor, Marc, V.J., the Foundation board and Natasha"],
 ["Julian Whitmore", "Does not know (per C-073)"]],
 [2.8*inch, 3.6*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Bernard 'Bunny' Washington", "4/19/1973 (32)", "Fetus in fetu, 18 cm, retroperitoneal, encapsulated", "Excision (Crump; Clayton; Marc)", "Recovering; burial with his mother"],
 ["Nadia Ellerbe", "4/25/1977 (28)", "Chorioamnionitis at 30w6d after PPROM and open fetal surgery", "Repeat cesarean through the hysterotomy scar (Clayton; Marc)", "Stable"],
 ["Malik Ellerbe Jr.", "11/4/2005", "Prematurity, 30w6d; post-fetal SCT resection", "NICU, CPAP", "Stable; home by Christmas expected"],
 ["Lap chole patient", "-", "Cholelithiasis", "Lap cholecystectomy (Lowery; Raven, Arianna)", "Uncomplicated"]],
 [1.1*inch, 0.85*inch, 1.75*inch, 1.75*inch, 0.95*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Bernard 'Bunny' Washington</b> (b. April 19, 1973), a Lenox Avenue barber. <b>Dr. Philip Grant</b> (b. March 13, 1976), a medicine resident. <b>Eddie</b> (b. 1965), a Monty's regular married to a Radiology tech.",
 "<b>Josephine 'Grandma Jo' Bullock</b> and <b>Dr. Grace Bullock</b> (voice) make their on-screen debuts (already in MA-005). <b>Malik Ellerbe Jr.</b> (b. November 4, 2005)."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["Rosa Parks died October 24, 2005, lay in honor in the Capitol Rotunda on October 30-31 (the first woman so honored), had a memorial at Metropolitan A.M.E. in Washington on October 31, and was buried in Detroit on November 2. "
 "Her quote: 'The only tired I was, was tired of giving in.' On November 4, 2005, the Summit of the Americas opened in Mar del Plata amid protests, and riots were in their eighth night in the Paris suburbs. Metrobus route 70 runs on Georgia Avenue.",
 "Medicine: fetus in fetu occurs in about 1 in 500,000 births. It is a vertebrate parasitic twin, usually retroperitoneal and encapsulated, distinguished from teratoma by an axial skeleton. Chorioamnionitis after PPROM is an indication for delivery. "
 "A 30-week neonate typically needs CPAP and goes home around 36-37 weeks corrected. Repeat cesarean after a classical hysterotomy is mandatory."])
