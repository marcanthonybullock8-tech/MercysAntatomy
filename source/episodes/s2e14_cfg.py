import os
from datetime import date
from reportlab.lib.units import inch
from ep_build import p, bl, tbl, H1, H2

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
OUT = os.path.join(D, '..', '..', 'PDFs', 'MA-S02E14_Little_White_Lies.pdf')
PARTS = [D + 's2e14_part1.txt', D + 's2e14_part2.txt', D + 's2e14_part3.txt']
EP = date(2006, 1, 20)
CODE = '2x14'
SEASON_LINE = 'Season 2, Episode 14'
TITLE = 'Little White Lies'
COUNTERPART = "Episode 2x14. The counterpart of <i>Grey's Anatomy</i> 2x14."
DATES = 'Friday, January 20, 2006, 5:48 AM through 11:58 PM'
DEPENDS = 'Depends on MA-001 through MA-011 and episodes 1x01-2x13'
AGES_ON = 'Friday, January 20, 2006'

CAST = [
 ("Dr. Harmony Divine", "Surgical Intern", date(1979,6,19)), ("Dr. Marc-Anthony Bullock", "Surgical Intern (narrator)", date(1979,1,5)),
 ("Dr. Amond Baker", "Surgical Intern", date(1979,2,10)), ("Darius 'Dash' Duvall", "Patient: Status 1A, day 70 (CVICU)", date(1971,8,8)),
 ("Dr. Raven Ellison", "Surgical Intern", date(1979,12,3)), ("Dr. Arianna Cummings", "Surgical Intern", date(1979,10,25)),
 ("Dr. Esther Smilley", "Surgical Intern", date(1979,9,20)), ("Dr. Bryce Kennerly", "Surgical Intern", date(1978,6,11)),
 ("Dr. Elxa Bullock", "Surgical Resident (37 weeks 2 days pregnant)", date(1977,8,29)), ("Mrs. Henrietta Bolden (new)", "Patient: atypical chest pain, facing eviction", date(1917,6,3)),
 ("Fulton Reese (new)", "Patient: three-vessel CAD, active smoker", date(1944,9,1)), ("Vernice Reese (new)", "Fulton's wife", date(1946,4,4)),
 ("Dr. Robert Bullock", "Chief of Cardiothoracic Surgery", date(1956,2,10)), ("Shanice Ward (new)", "Patient, age 15: ruptured ectopic pregnancy", date(1990,8,22)),
 ("Dr. Clayton Hartwell", "OB/GYN and Fetal Surgeon", date(1971,3,3)), ("Tiffany Royal (new)", "Patient: psychogenic nonepileptic seizures", date(1981,11,13)),
 ("Dr. Leland Graves", "Chief of Neurosurgery", date(1953,4,18)), ("Dr. Natasha Donohue", "Chief of Surgery", date(1958,6,2)),
 ("Bernadette 'Bernie' Watkins", "Executive Assistant to the Chief", date(1950,6,6)), ("Renee Ward (new)", "Shanice's mother; home attendant", date(1967,3,3)),
 ("Hattie 'Miss Hattie' Lomax", "Cafeteria", date(1945,3,3)), ("Nurse Gloria Pettiford", "Head ER Nurse", date(1952,4,14)),
 ("Nurse Yvette Banks", "CVICU Charge Nurse", date(1963,12,1)), ("Celia Montague, LCSW", "Hospital Social Worker", date(1966,5,6)),
 ("Lamont 'Monty' Gaines", "Owner, Monty's on Jackson", date(1962,10,10)), ("Lillian Divine", "Harmony's mother", date(1952,2,14)),
 ("Howard Divine", "Harmony's father", date(1950,8,30)), ("Mercy", "The House's pit bull puppy", date(2005,9,30)),
]
ALSO = ("<i>Also appearing: an elderly lung cancer patient and his son and daughter, a nurse, a registration clerk, a livery cab driver, and the EMU staff. "
        "Mentioned: James Frey, Oprah Winfrey, Dr. Harold Bynum, Dr. Delphine A. Ware (d. 2003), R. Adebayo, Esq., Augustin Toussaint, Jerry and Ronnie Divine, Dr. Hampton, Glenda Duvall and Malcolm Sloan.</i>")

MEDIA = [
 ("THE SMOKING GUN: \"A MILLION LITTLE LIES\"", "Posted January 8, 2006",
  ["\"Police reports, court records, interviews and other documents have exposed James Frey's memoir as a fabrication... Frey, whose book was an Oprah's Book Club selection, spent a few hours in a police station, not 87 days in jail...\" (The controversy dominated the third week of January 2006.)"]),
 ("ASSOCIATED PRESS: \"BIN LADEN TAPE WARNS OF ATTACKS, OFFERS 'TRUCE'\"", "Thursday, January 19, 2006",
  ["\"An audiotape attributed to Osama bin Laden and aired on Al-Jazeera warned of new attacks on the United States and offered a 'long-term truce.' The White House rejected the offer...\""]),
 ("QueensGraceConfidential (Blogger)", "Friday, January 20, 2006, 6:41 PM",
  ["<i>\"LIES, LIES, LIES. We're not naming names, but let's just say there is NO GYM ON VERNON and there is NO BALLY'S IN LIC. A certain someone has been 'at the gym' at 6 AM every day this week, and the gym has an IV pole. Pray for everybody involved. Truly. "
   "Also: an 88-year-old church mother who would only call one of our interns 'girl' all week signed out this evening saying 'Thank you, Dr. Divine' in front of the whole lobby. We witnessed it. We are not okay.\"</i> Comments (2,607)."]),
 ("Letter: Whitaker, Stein & Adebayo, LLP (Chicago) to Dr. Robert Bullock", "Forwarded by the Howard University alumni office; opened January 20, 2006",
  ["\"Dear Dr. Bullock: We represent the Estate of Delphine A. Ware, M.D., who passed away in Chicago in March 2003. Among Dr. Ware's papers was the enclosed sealed letter, with written instructions that it be delivered to you personally 'once the estate is settled.' The estate was settled on December 30, 2005. We have not read its contents. Sincerely, R. Adebayo.\" (Enclosure: one sealed envelope, 'Robert Bullock -- Personal.' UNOPENED.)"]),
 ("Abyssinian Development Corporation: Letter of Tenancy", "Friday, January 20, 2006",
  ["\"Mrs. Henrietta Bolden is approved for a one-bedroom senior unit at West 138th Street, effective February 1, 2006, at a monthly rent of $312. Elevator building.\""]),
 ("SMS, Motorola RAZR (Raven Ellison to Dash Duvall)", "Friday, January 20, 2006, 5:57 AM",
  ["<b>Raven:</b> \"on my way. decaf.\""]),
]

CONT = [p("Continuity Sheet: Episode 2x14", H1), p("New Canon Established", H2)]
CONT += bl([
 "<b>RAVEN, DASH AND ARIANNA:</b> Raven has been visiting Dash at 6 AM every day this week (decaf; Glenda calls her 'the angel') and telling Arianna she was at 'the gym.' Elxa caught the lie at the board ('There's no gym on Vernon'). Charge nurse Yvette Banks told Arianna, thinking she knew. <b>Arianna took her things from 49th Avenue in a tote bag:</b> 'I'm not breaking up with you. I'm taking a step back.' 'Fourteen words.' 'He's a good man, Raven.' Raven to Dash, her one true thing: 'I come because I can't stand to start a day without seeing you.' Dash admitted part of him is glad. <b>Arianna and Raven are 'on a step back,' not broken up.</b>",
 "<b>Marc lied twice for Raven</b> ('coffee,' then 'coffee after the gym'). Amond: 'Stop lying for people. It's not your truth to hold.' Amond revealed that for six months after his father's crash his mother told their church it was a 'heart attack.' <b>Marc told Arianna the whole truth</b> in Stairwell B: Raven loves her, she's falling for Dash, and she's terrified that choosing either one kills him.",
 "<b>ROBERT AND DELPHINE WARE:</b> a letter from Whitaker, Stein & Adebayo (Chicago), forwarded by the Howard alumni office, enclosed <b>a sealed letter from the late Dr. Delphine A. Ware</b> ('Robert Bullock -- Personal'), to be delivered once her estate settled (December 30, 2005). <b>Robert has NOT opened it.</b> It sits in the glove compartment of his silver Mercedes. He told Natasha it was 'alumni fund' and then 'Howard alumni of Chicago.' Natasha noticed the Chicago postmark: 'Secrets keep you sick... it won't keep forever.' He wrote a $5,000 check to Howard's Louis Stokes Health Sciences Library in both their names. <b>Per MA-005, the Mariah reveal stays in Season 11. The letter must remain unopened on screen until then.</b>",
 "<b>Harmony and Mrs. Henrietta Bolden</b> (88): she was a domestic worker on Park Avenue for 41 years and called Harmony 'girl' all week. She faked chest pain for four days because she faces eviction from 141st Street (52 years there; a condo conversion; the marshal's date is January 26). <b>Celia Montague</b> got her a senior unit on West 138th Street through the Abyssinian Development Corporation ($312 a month, elevator, February 1), and Legal Aid is filing a stay. Henrietta: 'Thank you, Dr. Divine... Don't you let anybody call you anything else.'",
 "<b>Augustin's move</b> (Saturday, January 14, Halsey Street): Jerry and Ronnie carried the bed up four flights. Augustin set the hotel photo on the windowsill himself, made chicory coffee and handed Harmony hers last, saying 'Merci, Mademoiselle Divine.' Esther's reading: 'Last is I'm thinking about it.'",
 "<b>Elxa (37w2d)</b> has had low back pain every 15 to 20 minutes since noon. <b>Natasha took over the surgical board herself</b> until 7 PM and sent Elxa home to call Dr. Hampton and Russell. Natasha ran the board in 1990 for six months. <b>Esther told Clayton about holding Marc's hand</b> at the vow renewal ('No more Octobers'). Clayton: 'I'd rather be terrified with the truth than comfortable with a lie.'",
 "<b>Kennerly told a family the plain truth about a lung mass</b> (Gloria: 'He doesn't lie. Half the attendings in this building can't say that'); the grandson is flying in from Fort Bragg. <b>Graves apologized to a patient</b> for saying 'faking' (PNES): 'I learned something from an intern today.' Arianna's Pittsburgh past: her father's lie was 'the VFW' when he was really at the corner of Penn and Highland, and at 15 she lied about her age to get a job at the Eat'n Park on McKnight Road. Lillian threw <i>A Million Little Pieces</i> in the trash."])
CONT.append(p("Knowledge Tracker (as of January 20, 2006)", H2))
CONT.append(tbl([["Item", "Who knows"],
 ["Raven's morning visits to Dash", "Everyone, including Arianna"],
 ["Raven's 'one true thing' to Dash", "Raven, Dash"],
 ["Delphine Ware's sealed letter", "Robert (unopened); Natasha knows only that there's a Chicago envelope he lied about"],
 ["Mariah Pettaway (Robert's daughter)", "No one. Locked until Season 11"],
 ["Elxa's early labor signs", "Elxa, Natasha, Russell, Dr. Hampton"]],
 [2.6*inch, 3.8*inch]))
CONT.append(p("Patient Registry", H2))
CONT.append(tbl([["Patient", "DOB / age", "Diagnosis", "Procedure / surgeon", "Outcome"],
 ["Mrs. Henrietta Bolden", "6/3/1917 (88)", "Atypical chest pain (cardiac and GI workup negative); housing crisis", "Social work intervention (Divine; Montague)", "Discharged; senior housing February 1"],
 ["Shanice Ward", "8/22/1990 (15)", "Ruptured right tubal ectopic, 7 weeks; claimed to be 18", "Laparoscopic right salpingectomy (Hartwell; Cummings)", "Stable; reconciled with her mother"],
 ["Fulton Reese", "9/1/1944 (61)", "Three-vessel CAD, 70% left main; cotinine 1,200 ng/mL", "Elective CABG postponed 4 weeks (R. Bullock; Baker)", "Patch, bupropion, counseling; gave up 'the pack'"],
 ["Tiffany Royal", "11/13/1981 (24)", "PNES (normal video EEG during events); childhood abuse", "AEDs tapered; psychiatry (Graves; Smilley; Bynum)", "Improving"],
 ["Elderly lung patient (ER)", "-", "6 cm right lung mass, malignant effusion", "Chest tube drainage (Kennerly)", "Palliative; family gathered"]],
 [1.1*inch, 0.85*inch, 1.75*inch, 1.75*inch, 0.95*inch]))
CONT.append(p("New Characters", H2))
CONT += bl(["<b>Mrs. Henrietta Bolden</b> (b. June 3, 1917), a domestic worker on Park Avenue from 1947 to 1988 who lived at West 141st Street from 1954. <b>Fulton Reese</b> (b. September 1, 1944), a retired Sanitation supervisor, and <b>Vernice</b> (b. April 4, 1946) of Springfield Gardens.",
 "<b>Shanice Ward</b> (b. August 22, 1990) and <b>Renee Ward</b> (b. March 3, 1967). <b>Tiffany Royal</b> (b. November 13, 1981), a home health aide. <b>Nurse Yvette Banks</b> and <b>Celia Montague, LCSW</b> make their on-screen appearances (in MA-005)."])
CONT.append(p("Real-World Accuracy Notes", H2))
CONT += bl(["The Smoking Gun's exposé of James Frey's <i>A Million Little Pieces</i> was posted January 8, 2006. Oprah defended him by phone on <i>Larry King Live</i> on January 11 and confronted him on her show on January 26. A bin Laden audiotape offering a 'truce' aired January 19, 2006. Howard's Louis Stokes Health Sciences Library opened in 2001. The Abyssinian Development Corporation operated senior housing in central Harlem. Eat'n Park is a Pittsburgh restaurant chain.",
 "Medicine: urine cotinine distinguishes active smokers (often several hundred to over 1,000 ng/mL) from passive exposure, and smoking cessation before elective CABG reduces pulmonary and wound complications. Kehr's sign (left shoulder pain from diaphragmatic irritation) suggests hemoperitoneum. A ruptured ectopic pregnancy is treated by salpingectomy, and a minor's pregnancy-related care is often confidential, though an emergency changes the clinical picture. "
 "Psychogenic nonepileptic seizures are confirmed by video EEG (no epileptiform activity; eye closure, side-to-side head movements and pelvic thrusting are suggestive), are not 'faking,' are strongly associated with trauma, and are treated with psychotherapy. A malignant pleural effusion is drained for palliation."])
