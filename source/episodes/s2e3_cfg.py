import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E03_Lose_Control.pdf')
PARTS = [D + 's2e3_part1.txt', D + 's2e3_part2.txt', D + 's2e3_part3.txt']
EP = date(2005, 10, 4)
CODE = '2x03'
SEASON_LINE = 'Season 2, Episode 3'
TITLE = 'Lose Control'
COUNTERPART = "Episode 2x03. The counterpart of <i>Grey's Anatomy</i> 2x03."
DATES = 'Tuesday, October 4, 2005, 4:41 AM through Wednesday, October 5, 2005, 5:15 AM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x02'
AGES_ON = 'Tuesday, October 4, 2005'

CAST = [
 ("Dr. Amond Baker", "Surgical Intern; patient", date(1979,2,10)), ("Miss Pearline (new)", "7 train passenger", date(1933,6,6)),
 ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)), ("Dr. Raven Ellison", "Surgical Intern", date(1979,12,3)),
 ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)), ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)),
 ("Dr. Arianna Cummings", "Surgical Intern", date(1979,10,25)), ("Dr. Bryce Kennerly", "Surgical Intern (back from suspension)", date(1978,6,11)),
 ("Dr. Elxa Bullock", "Surgical Resident (22 weeks pregnant)", date(1977,8,29)), ("Dr. Horace Whitlow", "Chief of Medicine", date(1949,9,19)),
 ("Nadia Ellerbe", "Patient: post-op open fetal surgery", date(1977,4,25)), ("Dr. Clayton Hartwell", "Fetal Surgeon", date(1971,3,3)),
 ("Malik Ellerbe", "Nadia's husband", date(1975,1,30)), ("Brother Kareem Shabazz (new)", "Patient: perforated duodenal ulcer", date(1953,2,21)),
 ("Sister Aminah Shabazz (new)", "Kareem's wife", date(1956,8,30)), ("Dr. Abraham Lowery", "Attending General Surgeon", date(1947,1,9)),
 ("Nurse Gloria Pettiford", "Head ER Nurse", date(1952,4,14)), ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)),
 ("Dr. Thaddeus Boykin (on-screen debut)", "Surgical Resident (PGY-3)", date(1975,8,2)), ("Dr. Natasha Donohue", "Chief of Surgery", date(1958,6,2)),
 ("Danielle Pryor-Hollis", "Patient: chemotherapy", date(1979,2,17)), ("Kevin Hollis", "Danielle's husband", date(1975,11,2)),
 ("Harriet Baker-Fenwick (debut)", "Amond's mother", date(1952,10,5)), ("Odile Lemieux", "Curtis's mother", date(1936,3,19)),
 ("Curtis Lemieux", "Patient: heart transplant", date(1961,4,9)), ("Tyrell Pickens", "Patient: GSW, second look", date(1989,6,7)),
 ("Lula Pickens", "Tyrell's grandmother", date(1941,2,11)), ("Kordell Pickens", "Tyrell's brother", date(1994,3,2)),
 ("Dr. Solomon Fenwick (debut)", "Amond's stepfather", date(1948,3,21)),
]
ALSO = ("<i>Also appearing: a scrub nurse, two anesthesiologists, a circulating nurse, trauma nurses, a fetal cardiologist and an infusion nurse. "
        "Mentioned: the CABG patient (a retired Con Ed engineer), Gwendolyn Monroe, the imam of the masjid on Sutphin Boulevard, and Russell Jeffries.</i>")

MEDIA = [
 ("ASSOCIATED PRESS: \"MUSLIMS IN U.S. BEGIN RAMADAN FAST\"", "Tuesday, October 4, 2005",
  ["\"Muslims across the United States began the monthlong Ramadan fast this week, abstaining from food and drink from dawn until sunset. "
   "Islamic law exempts the sick, travelers, pregnant women and others for whom fasting would be a hardship...\""]),
 ("NOBELPRIZE.ORG: The Nobel Prize in Physics 2005", "Tuesday, October 4, 2005",
  ["\"...awarded one half to Roy J. Glauber 'for his contribution to the quantum theory of optical coherence' and the other half jointly to John L. Hall and Theodor W. Hänsch 'for their contributions to the development of laser-based precision spectroscopy.'\""]),
 ("QueensGraceConfidential (Blogger)", "Tuesday, October 4, 2005, 2:40 PM",
  ["<i>\"Code in OR 2 this morning. Not a patient. An INTERN. Our spies say the cardiothoracic intern everyone is afraid of (you know the one: tailored scrubs, no small talk) went down mid-bypass. "
   "Six units. Lowery operated. Dr. X assisted and held something with two fingers that apparently kept him alive. The CT Chief kept sewing the whole time because he couldn't leave the table. "
   "Get well, Scary Intern. Nobody here is going to say it to your face, so we're saying it here.\"</i> Comments (533)."]),
 ("SMS, Motorola RAZR (Marc-Anthony Bullock and Amond Baker)", "Tuesday, October 4, 2005, 5:47 AM",
  ["<b>Marc:</b> \"u alive?\"", "<b>Amond:</b> \"Obviously.\""]),
 ("SMS, Motorola RAZR (Arianna Cummings to Marc-Anthony Bullock)", "Tuesday, October 4, 2005, 7:55 AM",
  ["<b>Arianna:</b> \"baker collapsed OR 2. GI bleed. big. go\""]),
 ("Dr. Kennerly's notebook (page 1)", "Tuesday, October 4, 2005",
  ["\"BULLOCK, M. -- from D.C. -- grandfather drove a bus (per Cummings) -- lives Hunters Pt w/ 3 roommates -- 'nice' -- Lowery let him assist (??) -- Chief smiles at him.\""]),
 ("SMS, Motorola RAZR (Amond Baker and Marc-Anthony Bullock)", "Wednesday, October 5, 2005, 5:15 AM",
  ["<b>Amond:</b> \"you're late.\"", "<b>Marc:</b> \"go back to sleep. the front bedroom's yours.\"", "<b>Amond:</b> \"we'll talk.\""]),
]

CONT = [p("Continuity Sheet: Episode 2x03", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>Amond's Meckel's diverticulum bled</b> on Tuesday, October 4, 2005, ten days before the scheduled October 14 surgery. He collapsed at 7:52 AM in OR 2 during Robert's CABG (an obtuse marginal graft), hit a Mayo stand, and his hemoglobin was 6.4, later 5.9. Robert could not leave the open chest. "
 "Lowery did an emergent laparotomy in OR 7 with <b>Marc assisting</b>, using 6 units of blood. Lowery resected 15 cm of ileum, including the 4 cm Meckel's and an ulcer that had eroded a mesenteric branch, about 55 cm from the ileocecal valve. "
 "<b>Marc held the bleeding mesenteric branch with two fingers for about 90 seconds</b> when a clamp slipped and the pressure fell to 60, then closed the common enterotomy. This is the R-4 counterpart of Cristina's ectopic rupture. Amond is expected to recover fully, per the No-Nerf rule.",
 "<b>Amond saw black stool at 11:52 PM on October 3</b> and didn't call Robert. He skipped his 5:15 AM 'you're late' text to Marc, the first time since August. Robert put him on <b>three weeks of medical leave</b> (from October 4, so back around October 25), still on Robert's service. Robert: 'Next time, press the button.' 'I know, son. But you are.'",
 "<b>Amond accepts the front second-floor bedroom</b> at the House on 49th Avenue ('we'll talk' means yes). He moves in during 2x04.",
 "<b>Harriet Baker-Fenwick</b> (her 53rd birthday is October 5) and <b>Dr. Solomon Fenwick</b> arrive from Los Angeles at 11:43 PM with four-cheese macaroni. 'Stomachaches since you were seven.' Odile Lemieux sat with Amond until Harriet came.",
 "<b>Raven heard Elxa say 'my brother'</b> in OR 3. Elxa denied it. Raven: 'It's like a password.' She asked Harmony; Harmony deflected ('he'll tell us when he's ready'). <b>Raven now strongly suspects Marc and Elxa are related.</b>",
 "<b>Whitlow connects Marc to Robert.</b> Arianna's cover story ('his grandfather drove a bus in D.C.'), passed on by Kennerly, matched Robert's CV ('son of Walter Bullock, WMATA Metrobus operator'). 'Not so common after all.' Kennerly is now Whitlow's informant on the medicine consult service. Whitlow also intends to raise 'supervision' (Robert and Amond) at the October 20 board meeting. Bernie saw the attending-CV binder on his desk.",
 "<b>Marc and Robert</b> in Stairwell C: 'That's the only plan anybody ever has. The rest is technique.' Natasha: 'We raised a man who runs toward the bleeding.'",
 "<b>Harmony</b> persuaded Brother Kareem Shabazz to accept surgery on the first day of Ramadan, citing Surah al-Baqarah 2:185 as Mrs. Gwendolyn Monroe taught it. <b>New canon:</b> Gwendolyn Monroe converted to Islam in 1985. Harmony tied a Graham patch with Dr. Boykin, and Lowery: 'That's two things I'll remember about today.'",
 "<b>Esther</b> (day 23) shaved Danielle Pryor-Hollis's head; Kevin shaved a stripe down his own. 'Don't let the calendar decide.' She agreed to dinner with Clayton on Thursday, October 6, after Dr. Greenidge, and turned her calendar face down.",
 "<b>Clayton</b> spotted Amond's anemia in the elevator ('the pale goes into the lips first') and doubled the blood-bank order. His line to Esther: 'You light up when you say his name.'",
 "<b>Kennerly</b> is back from suspension and on Whitlow's medicine consult service; his harassment hearing is 'next week.'"])
CONT.append(p("Knowledge Tracker (as of October 4, 2005)", H2))
CONT.append(tbl([["Secret", "Who knows", "New pressure"],
 ["Marc is Natasha and Robert's son", "Family, Bernie, Graves, Gloria, Mrs. Truitt, Amond, Big Ray, Arianna, Esther", "<b>Whitlow</b> has connected Marc to Robert; <b>Raven</b> suspects Marc is related to Elxa; Clayton suspects"],
 ["Marc is Victor's grandson", "Same, minus Monty", "Whitlow is circling the August 9 loading-dock visit"],
 ["Amond's illness", "Now the whole hospital (the blog)", "-"],
 ["Harmony loves Marc", "Raven, Esther", "-"]],
 [1.9*inch, 2.5*inch, 2.0*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Amond Baker", "2/10/1979 (26)", "Bleeding Meckel's diverticulum with ileal ulcer eroding a mesenteric branch; hemorrhagic shock (Hgb 5.9)", "Ex-lap, segmental ileal resection (15 cm), stapled anastomosis (Lowery; Marc)", "Stable; 6 units; leave 3 weeks"],
 ["Kareem Shabazz", "2/21/1953 (52)", "Perforated anterior duodenal ulcer (presumed H. pylori)", "Graham omental patch (Boykin; Harmony)", "Stable; NPO; H. pylori testing"],
 ["Tyrell Pickens", "6/7/1989 (16)", "Grade IV liver laceration, post-damage control", "Second look: packs removed, fascia closed (Elxa; Raven)", "Stable; clears tomorrow"],
 ["Nadia Ellerbe", "4/25/1977 (28)", "Preterm contractions, POD 1 after open fetal surgery", "Indomethacin and magnesium; fetal echo (Clayton; Marc)", "Contractions settling; 26w2d; ductus open"],
 ["CABG patient", "-", "Multivessel CAD", "CABG (Robert; fellow)", "Graft patent; home Friday"]],
 [1.05*inch, 0.9*inch, 1.75*inch, 1.7*inch, 1.0*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Brother Kareem Shabazz</b> (b. February 21, 1953), a South Jamaica Sunni Muslim who has fasted every Ramadan since 1976, and <b>Sister Aminah Shabazz</b> (b. August 30, 1956).",
 "<b>Harriet Baker-Fenwick</b> and <b>Dr. Solomon Fenwick</b> make their on-screen debuts (already in MA-005). <b>Dr. Thaddeus Boykin</b> (PGY-3) debuts on screen. <b>Miss Pearline</b> (b. 1933), a 7 train rider."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["Ramadan 1426 began in North America on or about October 4, 2005. The 2005 Nobel Prize in Physics (Glauber, Hall, Hänsch) was announced October 4. Surah al-Baqarah 2:184-185 exempts the sick from fasting.",
 "Medicine: a bleeding Meckel's diverticulum with ectopic gastric mucosa ulcerates the adjacent ileum, so segmental resection rather than a simple diverticulectomy is indicated. Hemorrhagic shock is managed with a rapid infuser and O-negative blood. "
 "A perforated duodenal ulcer is repaired with a Graham omental patch, followed by H. pylori eradication. Indomethacin tocolysis after fetal surgery requires serial fetal echocardiograms to watch for ductal constriction. "
 "Pulse steroids cause cushingoid facial changes ('moon face')."])
