import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E09_Thanks_for_the_Memories.pdf')
PARTS = [D + 's2e9_part1.txt', D + 's2e9_part2.txt', D + 's2e9_part3.txt']
EP = date(2005, 11, 24)
CODE = '2x09'
SEASON_LINE = 'Season 2, Episode 9'
TITLE = 'Thanks for the Memories'
COUNTERPART = "Episode 2x09. The counterpart of <i>Grey's Anatomy</i> 2x09."
DATES = 'Thursday, November 24, 2005 (Thanksgiving Day), 4:58 AM through 11:59 PM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x08'
AGES_ON = 'Thursday, November 24, 2005'

CAST = [
 ("Dr. Raven Ellison", "Surgical Intern (day off, cooking)", date(1979,12,3)), ("Dr. Amond Baker", "Surgical Intern", date(1979,2,10)),
 ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)), ("Dr. Natasha Donohue", "Chief of Surgery", date(1958,6,2)),
 ("Lillian Divine", "Harmony's mother", date(1952,2,14)), ("Howard Divine", "Harmony's father; MTA bus operator", date(1950,8,30)),
 ("Nurse Gloria Pettiford", "Head ER Nurse", date(1952,4,14)), ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)),
 ("Dr. Arianna Cummings", "Surgical Intern", date(1979,10,25)), ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)),
 ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)), ("Dr. Bryce Kennerly", "Surgical Intern (on probation)", date(1978,6,11)),
 ("Dr. Elxa Bullock", "Surgical Resident (29 weeks pregnant)", date(1977,8,29)), ("Dr. Isaiah Crump", "Chief of Pediatric Surgery", date(1944,3,11)),
 ("Desmond Royster (new)", "Patient: acute appendicitis", date(1997,2,19)), ("Shonda Royster (new)", "Desmond's mother; MTA station agent", date(1974,6,2)),
 ("Winston Teague", "Patient: LVAD, discharged", date(1947,1,22)), ("Pauline Teague", "Winston's wife", date(1950,9,30)),
 ("Dr. Victor Donohue", "Founder, Victor Donohue Foundation; Marc's grandfather", date(1933,5,30)), ("Dr. Clayton Hartwell", "Fetal Surgeon (on call, L&D)", date(1971,3,3)),
 ("Corinne Smilley (V.O.)", "Esther's mother", date(1948,7,22)), ("Deacon Theodore 'Teddy' Pritchard (new)", "Patient: Boerhaave syndrome", date(1946,4,9)),
 ("Hazel Pritchard (new)", "Teddy's wife", date(1948,1,30)), ("Leon Fairley (new)", "Patient: turkey-fryer burns", date(1958,7,16)),
 ("Duane (new)", "Leon's brother-in-law", date(1961,3,5)), ("Augustin Toussaint (on-screen debut)", "Camille's father; displaced New Orleans hotelier", date(1941,2,9)),
 ("Dr. Camille Toussaint", "Orthopedic Resident", date(1976,7,21)), ("Hattie 'Miss Hattie' Lomax", "Cafeteria", date(1945,3,3)),
 ("Dr. Horace Whitlow", "Chief of Medicine", date(1949,9,19)), ("Dr. Solomon Fenwick (V.O.)", "Amond's stepfather", date(1948,3,21)),
 ("Dr. Grace Bullock (on-screen debut)", "Harvard Medical School student; Marc's sister", date(1981,4,12)), ("Mother Viola Sturdivant (new)", "Patient: food bolus airway obstruction", date(1921,9,12)),
 ("Lorna Ellison (V.O., new)", "Raven's mother", date(1961,3,14)), ("Josephine 'Grandma Jo' Bullock (V.O.)", "Marc's paternal grandmother", date(1931,1,19)),
]
ALSO = ("<i>Also appearing: two EMTs, Viola Sturdivant's granddaughter, a fluoroscopy tech, L&D and CVICU nurses, a scrub nurse, Victor's driver, and Jerry and Ronnie Divine (off-screen). "
        "Mentioned: Dr. Joan Mercer, Claudette and V.J. Donohue, Russell Jeffries (by phone), Dr. Lowery (in Maryland), Malcolm Sloan, Lucius Donohue, Aunt Clarice and Dr. Yolanda Fitch.</i>")

MEDIA = [
 ("ASSOCIATED PRESS: \"WIND-WHIPPED BALLOON HITS LAMPPOST, INJURING 2 AT MACY'S PARADE\"", "Thursday, November 24, 2005",
  ["\"NEW YORK (AP) -- A giant M&M's balloon struck a lamppost in Times Square during the Macy's Thanksgiving Day Parade on Thursday, injuring two sisters, police said. The injuries were minor. Since a 1997 accident, the city has restricted balloon heights in high winds...\""]),
 ("THE DENVER POST (Sports): \"BRONCOS TAKE TURKEY IN OT\"", "Friday, November 25, 2005",
  ["\"IRVING, Texas -- Denver beat Dallas 24-21 in overtime on Thanksgiving Day on a field goal by Jason Elam...\" Earlier, the Falcons beat the Lions, 27-7, in Detroit. The displaced Saints split their 2005 'home' games between San Antonio's Alamodome and Baton Rouge."]),
 ("QueensGraceConfidential (Blogger)", "Thursday, November 24, 2005, 3:12 PM",
  ["<i>\"HAPPY THANKSGIVING FROM THE FIFTH FLOOR. A certain intern's mother (the hat, the van, the PIES) fed the ENTIRE hospital again. Sources say even a certain Chief of Medicine ate a plate. Both turkey AND ham. "
   "Also: the Chief's son reportedly diagnosed a ruptured esophagus this morning and then had to hand the case to... his own father, per the Firewall. Imagine Thanksgiving dinner. Actually, don't. We hear the Old Man himself is AT that dinner. In an apron. We cannot confirm the apron. We are begging someone to confirm the apron.\"</i> Comments (803)."]),
 ("Index card: \"JO'S ROLLS\" (Josephine Bullock's recipe, in her hand)", "Written c. 1974; used November 24, 2005",
  ["\"1 pkg yeast. 1/4 c warm water. 1 c scalded milk. 1/4 c sugar. 1/4 c Crisco. 1 egg. 4 c flour. Knead 10 min -- DON'T CHEAT, ROBERT. Rise 1 hr. Shape. Rise again. 400 degrees, 15 min. Brush with butter while hot.\""]),
 ("Note taped to a foil plate (Lillian Divine)", "Thursday, November 24, 2005",
  ["\"Eat all of it. -Mrs. D.\""]),
 ("SMS, Motorola RAZR (Harmony Divine to Raven Ellison)", "Thursday, November 24, 2005, 11:58 AM",
  ["<b>Harmony:</b> \"is victor really peeling potatoes\"", "<b>Raven:</b> \"he does it in ONE PEEL. one. im going to faint\"", "<b>Harmony:</b> \"dont faint on the turkey\""]),
]

CONT = [p("Continuity Sheet: Episode 2x09", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>Thanksgiving at 49th Avenue:</b> Victor (head of the table), Natasha, Robert, Grace, Marc, Esther, Raven, Arianna, Harmony, Camille, Augustin and Amond, twelve in all. Victor arrived at 8:47 AM with a Make My Cake sweet potato pie (bought, not baked, per his promise) and a chef's apron, and cooked with Raven all day. Robert made Grandma Jo's rolls for the first time since Walter Bullock's funeral in 1999 (36 rolls). Amond bought a white porcelain gravy boat. Victor's toast: 'To the memories.'",
 "<b>Victor and Robert:</b> the first real thaw in 27 years. Victor: 'You've never thanked me for anything.' Robert: 'You never let me pay for anything I could thank you for.' Victor did <i>not</i> arrange Robert's Hopkins fellowship (Robert had assumed he did). Victor said Robert's rolls are 'better than Josephine's,' and Marc told Grandma Jo that night. Victor skipped the Brookline Thanksgiving (31 Donohues; Joan told V.J. he was 'seeing to the future'). On the stoop he told Marc: 'Next year, everyone will know why I came.' <b>The heir designation is still secret.</b>",
 "<b>Victor's family history:</b> his father's brother Lucius quarreled with Victor's father in 1946 over land in Prince Edward County, Virginia. His father wrote every Christmas for 22 years, and Lucius died in 1968 with the letters unopened. Victor's father had 'buried a son,' so Victor had a brother who died (details to come). At Freedmen's in 1957 Victor peeled 400 potatoes for patients' Thanksgiving. He stayed at the Hotel Toussaint in 1978, and Augustin sent champagne to every Black doctor there.",
 "<b>Raven called her mother.</b> Lorna Ellison (Savannah, MLK Blvd.) answered at 7:09 PM. It was the first time Raven had heard her voice in six years. Lorna has 1,079 days clean and follows QGH news on library computers. Raven said: 'I'm a surgeon. In New York.' Arianna sat with her. Raven has Lorna's number on her nightstand. Victor's advice ('I don't believe in letting things be') pushed her to call.",
 "<b>Elxa, 29 weeks:</b> contractions every 8 minutes from noon. Cervical length 3.8 cm, closed; fetal fibronectin negative; reactive strip. Diagnosis: dehydration and Braxton Hicks. One liter of fluid, then home with Russell. She told Clayton not to call Natasha, and he called anyway. Natasha left the dinner to read the strip herself, approved Clayton's read ('That's why I'll keep him') and brought Esther back to the house: 'Nobody eats alone on Thanksgiving.' Natasha's story: on Thanksgiving 1977 she sat all night at Mount Auburn Hospital with three-month-old Elxa, who had a fever of 103.",
 "<b>Harmony and Camille:</b> Augustin Toussaint (64) makes his on-screen debut. He's sleeping on a cousin's couch in Canarsie and wears his only surviving suit daily. He lost the house on Elysian Fields, the Hotel Toussaint on Esplanade and his wife's grave (under 11 feet of water). Camille introduced Harmony as 'my friend' twice. <b>Augustin walked in on a tender moment in the kitchen</b> and said nothing ('Tell her an old man from New Orleans said so'). Whether he knows is deliberately ambiguous.",
 "<b>Amond called Solomon first</b> ('I called for you, Sol'), from the roof, not a stairwell, as Robert advised. Solomon drove him to the 1990 science fair and waited six hours. Amond did the Boerhaave repair under Robert. <b>Marc diagnosed it but couldn't scrub</b> (Firewall). Robert: 'Then I'll tell Deacon Pritchard who found it.'",
 "<b>Arianna:</b> Crump quizzed her through an appendectomy: 'You're not answering the questions. You're answering your father.' Crump failed the written surgical boards in 1971 and passed the next year with the highest score in New York State. He told Desmond Royster that Arianna will be 'a doctor for kids' (foreshadowing her peds track). Desmond quizzed her with the purple cards.",
 "<b>Kennerly</b> pulled a turkey bolus from Viola Sturdivant's airway with Magill forceps. Lillian Divine left him a plate ('Eat all of it. -Mrs. D.'). Kennerly told Marc the Monopoly cards weren't him. Marc: 'You'd have used real money.' <b>Whitlow ate Lillian's food</b> in the cafeteria and learned she is Harmony's mother.",
 "<b>Howard Divine's CT is scheduled for December 8, 2005</b> at Jamaica Hospital (the 6 mm RUL nodule, per MA-005). His cough continues, with no blood. <b>Grace Bullock's on-screen debut</b> (24): Acela from Boston, 'Gracepedia' facts, and she bonds with Amond over dishes. Clayton and Esther talked about going to Mattapan next year 'if there won't be an empty chair.' Winston Teague went home on day 15 and played brushes for the CVICU; Amond is invited to the June wedding."])
CONT.append(p("Knowledge Tracker (as of November 24, 2005)", H2))
CONT.append(tbl([["Item", "Who knows"],
 ["Heir designation", "Still secret: Victor, Marc, V.J. (not the content), the Foundation board, Natasha and Joan"],
 ["Harmony and Camille are together", "The housemates, Grace (likely), Augustin (ambiguous)"],
 ["Raven called her mother", "Arianna; the whole table (Raven's toast)"],
 ["Elxa's contraction scare", "Natasha, Robert, Clayton, Esther, Gloria, Russell, the table"],
 ["Howard's nodule / CT date", "The Divines, Harmony"]],
 [2.6*inch, 3.8*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Deacon Teddy Pritchard", "4/9/1946 (59)", "Boerhaave syndrome (2.5 cm distal left tear) after a prayer breakfast", "Left thoracotomy, two-layer repair, intercostal flap (R. Bullock; Baker)", "Repaired within 6 hours; good prognosis"],
 ["Desmond Royster", "2/19/1997 (8)", "Acute appendicitis (Alvarado 8), non-perforated", "Laparoscopic appendectomy (Crump; Cummings)", "Recovering"],
 ["Leon Fairley", "7/16/1958 (47)", "Partial-thickness burns, both hands and forearms, facial flash (frozen turkey in a fryer)", "Stabilized (Bullock; Kennerly)", "Transferred to Weill Cornell Burn Center"],
 ["Mother Viola Sturdivant", "9/12/1921 (84)", "Supraglottic food bolus obstruction (turkey)", "Laryngoscopy, Magill forceps extraction (Kennerly)", "Revived: 'Never again'"],
 ["Dr. Elxa Bullock", "8/29/1977 (28)", "Contractions at 29w0d; dehydration", "IV fluids, monitoring (Hartwell; Donohue reviewed)", "FFN negative; discharged home"],
 ["Winston Teague", "1/22/1947 (58)", "LVAD destination therapy, post-op day 15", "Discharge (Baker)", "Home for Thanksgiving"]],
 [1.1*inch, 0.85*inch, 1.75*inch, 1.75*inch, 0.95*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Augustin Toussaint</b> (b. February 9, 1941), on-screen debut. <b>Lorna Ellison</b> (b. March 14, 1961), voice debut; she had Raven at 18. <b>Grace Bullock</b>, on-screen debut (in MA-005).",
 "<b>Deacon Teddy Pritchard</b> (b. April 9, 1946, Antioch Baptist usher) and <b>Hazel</b> (b. January 30, 1948). <b>Desmond Royster</b> (b. February 19, 1997) and <b>Shonda</b> (b. June 2, 1974). <b>Leon Fairley</b> (b. July 16, 1958) of Hollis and <b>Duane</b> (b. March 5, 1961). <b>Mother Viola Sturdivant</b> (b. September 12, 1921)."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["On Thanksgiving, November 24, 2005, high winds at the Macy's parade drove the M&M's balloon into a Times Square lamppost, injuring two sisters (minor injuries). The Broncos beat the Cowboys 24-21 in overtime, and the Falcons beat the Lions 27-7. "
 "The displaced 2005 Saints played home games in San Antonio and Baton Rouge. The first Macy's parade (1924) used Central Park Zoo animals, and balloons began in 1927 with Felix the Cat. Charles Pratt's Astral Oil Works stood on Newtown Creek ('The holy lamps of Tibet are primed with Astral Oil'). "
 "Flint-Goodridge Hospital in New Orleans closed in 1983. Make My Cake is a Harlem bakery.",
 "Medicine: Boerhaave syndrome (spontaneous transmural esophageal rupture, usually distal left posterolateral) presents with Mackler's triad (vomiting, chest pain, subcutaneous emphysema) and Hamman's crunch, and is confirmed by a water-soluble contrast swallow. "
 "Repair within 24 hours (two-layer closure with a muscle flap through a left thoracotomy) greatly lowers mortality. A negative fetal fibronectin has a very high negative predictive value (about 99%) for delivery within 14 days. "
 "Hand and face burns meet burn center referral criteria regardless of %TBSA. A supraglottic food bolus is removed with Magill forceps under direct laryngoscopy. The Alvarado score is used for appendicitis."])
