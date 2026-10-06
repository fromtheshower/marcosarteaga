"""Reviewed Québec French copy for the audit and privacy pages."""

def pairs(data: str) -> dict[str, str]:
    return dict(line.split('\t', 1) for line in data.strip().splitlines())

TEXT = pairs("""
Marcos Arteaga | Independent Paid Media Audits\tMarcos Arteaga | Audits indépendants de publicité numérique
Privacy Policy | Marcos Arteaga\tPolitique de confidentialité | Marcos Arteaga
Skip to content\tAller au contenu
Book the audit\tDemander un audit
Paid-media audits · Google · Meta · TikTok · Snapchat\tAudits publicitaires · Google · Meta · TikTok · Snapchat
Your ad account is leaking money. I’ll show you exactly where.\tVotre compte publicitaire perd de l’argent. Je vous montrerai où.
A fixed-scope audit of your Google Ads, Meta Ads, TikTok Ads, or Snapchat Ads accounts, delivered in 10 business days. Every finding backed by your own data. No retainer. No fluff.\tUn audit à portée fixe de vos comptes Google Ads, Meta Ads, TikTok Ads ou Snapchat Ads, livré en 10 jours ouvrables. Chaque constat s’appuie sur vos données. Pas de mandat mensuel. Pas de blabla.
Independent diagnosis\tDiagnostic indépendant
Prioritized next steps\tActions classées par priorité
Personally by Marcos\tRéalisé par Marcos lui-même
The audit\tL’audit
Not a checklist.\tPas une liste à cocher.
A diagnosis.\tUn diagnostic.
I look for the decisions, settings, and measurement gaps that cost you money. Then I tell you what deserves attention.\tJe cherche les décisions, réglages et lacunes de mesure qui vous coûtent de l’argent. Ensuite, je vous dis ce qui mérite vraiment votre attention.
Structure review\tAnalyse de la structure
Campaigns, budgets, bidding. Is the account built to learn, or built to leak?\tCampagnes, budgets, enchères. Le compte est-il construit pour apprendre ou pour gaspiller?
Waste hunt\tRecherche des dépenses inutiles
Search terms, placements, audience overlap, location and device bleed, and broken negatives. Findings come with evidence from your data.\tTermes de recherche, emplacements, chevauchement des audiences, ciblage géographique et appareils, mots-clés à exclure défaillants. Chaque constat est étayé par vos données.
Tracking check\tVérification du suivi
Conversion setup and attribution. Can you trust the numbers you’re optimizing toward?\tConfiguration des conversions et attribution. Pouvez-vous vous fier aux chiffres qui guident vos décisions?
Message check\tVérification du message
Does the ad promise match the landing page? A focused review, not creative production.\tLa promesse de l’annonce correspond-elle à la page de destination? Une analyse ciblée, pas de la création publicitaire.
The call\tLa décision
A prioritized fix list: do this week, do this month, leave alone. Prioritization is the product.\tUne liste de correctifs par priorité : cette semaine, ce mois-ci, ou à laisser tranquille. La priorisation, c’est le produit.
What you get\tCe que vous recevez
A written report backed by your account data. A prioritized action plan. A 60-minute walkthrough where I defend every line.\tUn rapport écrit fondé sur les données de votre compte. Un plan d’action priorisé. Une rencontre de 60 minutes où j’explique et défends chaque recommandation.
The business numbers:\tLes vrais chiffres d’affaires :
MER from actual sales and the ad spend in scope; paid CAC from spend and new-customer counts. ROAS checked against sales records, not just platform-attributed numbers, with attribution limits called out.\tLe MER calculé à partir des ventes réelles et des dépenses publicitaires analysées; le CAC payant à partir des dépenses et du nombre de nouveaux clients. Le ROAS est comparé aux ventes réelles, pas seulement aux conversions attribuées par les plateformes, avec les limites d’attribution expliquées.
10 business days from kickoff and access.\t10 jours ouvrables après la rencontre de départ et l’obtention des accès.
Read-only access and kickoff → analysis → report and walkthrough. If I need longer, you’ll hear about it before, not after.\tAccès en lecture seule et rencontre de départ → analyse → rapport et présentation. Si j’ai besoin de plus de temps, je vous le dirai avant, pas après.
The fit\tÀ qui s’adresse l’audit
A clear answer.\tUne réponse claire.
A clear boundary.\tUn cadre clair.
This is for you if\tC’est pour vous si
You spend at least $5,000 a month (CAD in Canada, USD in the US) across Google Ads, Meta Ads, TikTok Ads, or Snapchat Ads.\tVous dépensez au moins 5 000 $ par mois (en dollars canadiens au Canada ou en dollars américains aux États-Unis) sur Google Ads, Meta Ads, TikTok Ads ou Snapchat Ads.
You suspect the account underperforms but nobody can say exactly why.\tVous pensez que le compte pourrait mieux performer, mais personne ne peut dire précisément pourquoi.
You want an independent read from someone who does not manage your account.\tVous voulez l’avis indépendant d’une personne qui ne gère pas votre compte.
It isn’t for you if\tCe n’est pas pour vous si
Your monthly ad spend is below roughly $5,000 (CAD in Canada, USD in the US). The economics usually don’t work.\tVos dépenses publicitaires sont inférieures à environ 5 000 $ par mois (en dollars canadiens au Canada ou en dollars américains aux États-Unis). Le calcul en vaut rarement la peine.
You want ongoing account management or creative production.\tVous cherchez une gestion continue du compte ou de la création publicitaire.
You only want an automated checklist.\tVous voulez seulement une liste de vérification automatisée.
The boundary:\tLa limite :
I don’t operate accounts myself. That keeps the diagnosis independent. Your team can run the fixes from my roadmap, or a vetted partner agency can implement them under a separate engagement quoted after the audit. The audit includes no ongoing management, creative production, or guaranteed ROAS lift.\tJe ne gère pas les comptes moi-même. C’est ce qui garde mon diagnostic indépendant. Votre équipe peut appliquer les correctifs à partir de ma feuille de route, ou une agence partenaire sélectionnée peut le faire dans le cadre d’un mandat distinct, proposé après l’audit. L’audit ne comprend ni gestion continue, ni création publicitaire, ni garantie d’amélioration du ROAS.
How I think\tMa façon de réfléchir
Where the leaks come from.\tD’où viennent les pertes.
Three illustrative scenarios, not client results. The actual call comes from your account data.\tTrois scénarios fictifs pour illustrer ma méthode, pas des résultats clients. Le vrai diagnostic vient des données de votre compte.
Tracking\tSuivi
What I see\tCe que je vois
Platform-reported conversions drive every decision. A purchase event fires twice, and nobody has checked it against actual sales.\tToutes les décisions reposent sur les conversions déclarées par la plateforme. Un achat est compté deux fois, et personne n’a vérifié les chiffres contre les ventes réelles.
Reconcile platform conversions with sales records. Fix measurement, then optimize.\tComparer les conversions de la plateforme aux ventes réelles. Corriger la mesure, puis optimiser.
Why it matters\tPourquoi c’est important
The problem isn’t “ROAS dropped.” It’s steering by a number you can’t trust.\tLe problème n’est pas « le ROAS a baissé ». C’est de prendre des décisions à partir d’un chiffre peu fiable.
Incrementality\tIncrémentalité
Prospecting campaigns keep reaching people who already bought. The report counts returning buyers as new demand.\tLes campagnes de prospection touchent encore des personnes qui ont déjà acheté. Le rapport compte ces clients comme une nouvelle demande.
Exclude known buyers where the platform allows. Separate brand demand from prospecting, with a distinct budget and objective for each.\tExclure les acheteurs connus lorsque la plateforme le permet. Séparer la demande liée à la marque de la prospection, avec un budget et un objectif distincts pour chacune.
The problem isn’t just rising CPA. It’s paying to claim customers you already had.\tLe problème n’est pas seulement la hausse du CPA. C’est de payer pour revendiquer des clients que vous aviez déjà.
Feed\tFlux de produits
In a Shopping account, products are disapproved or miscategorized. Best sellers barely serve.\tDans un compte Shopping, des produits sont refusés ou mal catégorisés. Les meilleurs vendeurs s’affichent à peine.
Fix titles, categories, and availability in the product feed before increasing Shopping spend.\tCorriger les titres, les catégories et la disponibilité dans le flux de produits avant d’augmenter les dépenses Shopping.
The problem isn’t “Shopping doesn’t work for us.” The feed is the ad—and yours is broken.\tLe problème n’est pas que « Shopping ne fonctionne pas pour nous ». Le flux est l’annonce, et le vôtre est défaillant.
Independent judgment\tJugement indépendant
Google’s AI works for Google.\tL’IA de Google travaille pour Google.
Automated recommendations can flag settings. They can’t own your tradeoffs or defend which fix comes first. I read the account, the measurement, and the path to conversion. Then I make the call: what to fix now, what can wait, and what to leave alone.\tLes recommandations automatisées peuvent signaler des réglages. Elles ne peuvent pas assumer vos compromis ni défendre l’ordre des correctifs. J’examine le compte, la mesure et le parcours jusqu’à la conversion. Puis je décide quoi corriger maintenant, quoi reporter et quoi laisser tranquille.
And the chatbots can’t do this either.\tEt les agents conversationnels ne peuvent pas faire ça non plus.
Without a direct connection, ChatGPT and Claude can only read what you hand them—screenshots and exports that may miss the path from spend to conversion. I get read-only access to your ad accounts and analytics, make the priority call, and defend it on a live 60-minute call. And pasting your business’s numbers into a chatbot is a data-sharing decision you shouldn’t make lightly.\tSans connexion directe, ChatGPT et Claude ne peuvent lire que ce que vous leur donnez : captures d’écran et exports qui peuvent manquer le parcours entre la dépense et la conversion. J’accède à vos comptes publicitaires et à vos données analytiques en lecture seule, je fixe les priorités et je défends mes choix lors d’un appel de 60 minutes. Copier les chiffres de votre entreprise dans un agent conversationnel est aussi une décision de partage de données à prendre au sérieux.
About Marcos\tÀ propos de Marcos
A specialist,\tUn spécialiste,
not another dashboard.\tpas un autre tableau de bord.
I’m Marcos Arteaga. I’ve worked across fashion retail, DTC, SaaS, B2B, and publishing. I now focus on one job: finding where paid media accounts leak money and giving you a plan you can actually use.\tJe suis Marcos Arteaga. J’ai travaillé dans la mode, la vente directe aux consommateurs, le SaaS, le B2B et l’édition. Aujourd’hui, je me concentre sur une chose : trouver où les comptes publicitaires perdent de l’argent et vous donner un plan que vous pouvez vraiment utiliser.
Selected experience\tExpérience sélectionnée
Questions\tQuestions
Before you book.\tAvant de réserver.
How is this different from my agency’s audit?\tEn quoi cet audit diffère-t-il de celui de mon agence?
Your agency has to evaluate work it already owns. I don’t run your account, so I have nothing to defend. You get an independent diagnosis.\tVotre agence doit évaluer son propre travail. Je ne gère pas votre compte; je n’ai donc rien à défendre. Vous obtenez un diagnostic indépendant.
What do you need from me?\tDe quoi avez-vous besoin?
Read-only access to your ad accounts, analytics, and sales data (Shopify or equivalent). Nothing gets changed. We start with a 20-minute kickoff call.\tUn accès en lecture seule à vos comptes publicitaires, à vos données analytiques et à vos ventes (Shopify ou l’équivalent). Rien n’est modifié. Nous commençons par un appel de 20 minutes.
What if you find nothing major?\tEt si vous ne trouvez rien de majeur?
Then I’ll say so. You’ll see what I checked, what held up, and what I’d leave alone. I won’t invent a problem to fill a report.\tJe vous le dirai. Vous verrez ce que j’ai vérifié, ce qui fonctionne et ce que je laisserais tel quel. Je n’inventerai pas un problème pour remplir un rapport.
Do you implement the fixes?\tAppliquez-vous les correctifs?
Yes, through a vetted partner agency. They can implement from my audit roadmap under a separate engagement, quoted after the audit. Your team can also run the plan. I stay out of the account so the diagnosis stays independent.\tOui, par l’entremise d’une agence partenaire sélectionnée. Elle peut appliquer les correctifs de ma feuille de route dans le cadre d’un mandat distinct, proposé après l’audit. Votre équipe peut aussi suivre le plan. Je ne touche pas au compte pour préserver l’indépendance du diagnostic.
Why a flat fee instead of hourly?\tPourquoi un forfait plutôt qu’un tarif horaire?
Because you’re buying the answer, not my time. The scope and fee are agreed privately before the audit begins.\tParce que vous achetez une réponse, pas mes heures. La portée et le forfait sont convenus en privé avant le début de l’audit.
The next step\tLa prochaine étape
Book the audit.\tDemander un audit.
Tell me what’s happening in the account. I’ll reply personally within 2 business days about fit and next steps.\tDites-moi ce qui se passe dans votre compte. Je vous répondrai personnellement sous 2 jours ouvrables au sujet de l’adéquation et des prochaines étapes.
No account access needed to send an enquiry. If we work together, access is read-only.\tAucun accès au compte n’est nécessaire pour m’écrire. Si nous travaillons ensemble, l’accès sera en lecture seule.
Fixed scope. Flat fee. No ongoing management.\tPortée fixe. Forfait fixe. Aucune gestion continue.
Name\tNom
Email\tCourriel
Website\tSite Web
Country\tPays
Select your country\tChoisissez votre pays
Canada\tCanada
United States\tÉtats-Unis
Spend ranges are in CAD for Canada and USD for the US.\tLes tranches de dépenses sont en dollars canadiens pour le Canada et en dollars américains pour les États-Unis.
Monthly ad spend\tDépenses publicitaires mensuelles
Select a range\tChoisir une tranche
Under $5,000/month\tMoins de 5 000 $/mois
$5,000–$15,000/month\t5 000 $ à 15 000 $/mois
$15,000–$50,000/month\t15 000 $ à 50 000 $/mois
$50,000+/month\t50 000 $ et plus/mois
Platforms\tPlateformes
Choose all that apply.\tCochez toutes les plateformes pertinentes.
Other platform (ask about fit)\tAutre plateforme (à discuter)
Which other platform?\tQuelle autre plateforme?
The audit is designed for accounts spending at least $5,000 a month. You can still send a note; I’ll give you an honest answer about fit.\tL’audit est conçu pour les comptes qui dépensent au moins 5 000 $ par mois. Vous pouvez quand même m’écrire; je vous dirai franchement si c’est le bon moment.
What’s bothering you about your account?\tQu’est-ce qui vous préoccupe dans votre compte?
Leave this field blank\tLaissez ce champ vide
I’ll use these details to reply about your audit enquiry.\tJ’utiliserai ces renseignements pour répondre à votre demande d’audit.
How I handle your information\tComment je traite vos renseignements
Send audit enquiry\tEnvoyer la demande d’audit
Enquiry sent\tDemande envoyée
Thanks for reaching out.\tMerci de m’avoir écrit.
I’ll reply personally within 2 business days about fit and next steps.\tJe vous répondrai personnellement sous 2 jours ouvrables au sujet de l’adéquation et des prochaines étapes.
Privacy\tConfidentialité
Blog\tBlogue (EN)
The plain version\tEn clair
Privacy policy.\tPolitique de confidentialité.
Last updated: October 2026\tDernière mise à jour : octobre 2026
You send an audit enquiry. I use it to answer you. Here’s what happens to the information you share.\tVous m’envoyez une demande d’audit. Je l’utilise pour vous répondre. Voici ce qui arrive aux renseignements que vous me confiez.
What I collect\tCe que je recueille
When you send an audit enquiry, I collect what you type into the form: your name, email address, website, country, monthly ad spend range, the platforms you use, and your message. If you choose “Other platform,” I collect the platform you name. No account access is needed—or asked for—at the enquiry stage.\tQuand vous envoyez une demande d’audit, je recueille ce que vous inscrivez dans le formulaire : votre nom, votre adresse courriel, votre site Web, votre pays, votre tranche de dépenses publicitaires mensuelles, les plateformes utilisées et votre message. Si vous choisissez « Autre plateforme », je recueille aussi le nom de cette plateforme. Aucun accès à vos comptes n’est nécessaire ni demandé à cette étape.
The web host may log standard request details, such as your IP address. To limit spam, the form keeps a hashed IP key and submission times in a server temporary file.\tL’hébergeur peut conserver les données techniques habituelles des requêtes, comme votre adresse IP. Pour limiter les pourriels, le formulaire conserve une clé dérivée de l’adresse IP et l’heure des envois dans un fichier temporaire sur le serveur.
Why I collect it\tPourquoi je les recueille
To reply to your enquiry about fit and next steps. That’s the purpose. The form sends a short automatic acknowledgement; I follow up personally. The technical details keep the form running and limit spam.\tPour répondre à votre demande et discuter de l’adéquation et des prochaines étapes. C’est le but. Le formulaire envoie un bref accusé de réception automatique; je vous réponds ensuite personnellement. Les données techniques servent au fonctionnement du formulaire et à la prévention des pourriels.
What I don’t do\tCe que je ne fais pas
I don’t add you to any marketing or newsletter list. I don’t sell or rent your information. I use what you type only to respond to your enquiry. I don’t pass it to a partner agency unless you choose a separate implementation engagement.\tJe ne vous ajoute à aucune liste marketing ni infolettre. Je ne vends ni ne loue vos renseignements. J’utilise ce que vous inscrivez uniquement pour répondre à votre demande. Je ne le transmets pas à une agence partenaire à moins que vous choisissiez un mandat distinct de mise en œuvre.
Where it goes\tOù vont vos renseignements
Enquiries are emailed to me at\tLes demandes me sont envoyées par courriel à
through Google Workspace. The site runs on a Plesk web host. Both providers process information needed to run the site and deliver the email; their systems may process it outside Québec.\tpar Google Workspace. Le site est hébergé sur un serveur Plesk. Ces deux fournisseurs traitent les renseignements nécessaires à l’exploitation du site et à l’envoi des courriels; leurs systèmes peuvent traiter ces données à l’extérieur du Québec.
If we end up working together, the audit itself runs on read-only access to your ad accounts, analytics, and sales data. Nothing gets changed, and your data stays yours.\tSi nous travaillons ensemble, l’audit repose sur un accès en lecture seule à vos comptes publicitaires, à vos données analytiques et à vos ventes. Rien n’est modifié, et vos données restent les vôtres.
How long I keep it\tCombien de temps je les conserve
If we don’t work together, I delete enquiry details within 12 months. If we do, they’re kept for the duration of our working relationship, and longer only if the law requires it. The host’s technical logs and the form’s spam-control records are kept separately for site operation and security.\tSi nous ne travaillons pas ensemble, je supprime les renseignements liés à votre demande dans les 12 mois. Sinon, je les conserve pendant notre relation de travail, et plus longtemps seulement si la loi l’exige. Les journaux techniques de l’hébergeur et les données antipourriel du formulaire sont conservés séparément pour le fonctionnement et la sécurité du site.
Your rights\tVos droits
Under Québec’s Law 25, you can ask to see or correct your personal information, withdraw consent where applicable, or ask me to delete it. Legal retention requirements may limit deletion. Email\tSelon la Loi 25 du Québec, vous pouvez demander à consulter ou à corriger vos renseignements personnels, retirer votre consentement lorsque cela s’applique, ou me demander de les supprimer. Les obligations légales de conservation peuvent limiter la suppression. Écrivez à
and I’ll handle it personally.\tet je m’en occuperai personnellement.
Privacy officer\tResponsable de la protection des renseignements personnels
Home\tAccueil
""")

ATTRS = pairs("""
Independent audits of Google, Meta, TikTok, and Snapchat Ads. Find wasted spend, check tracking, and leave with a prioritized fix plan.\tAudits indépendants de Google, Meta, TikTok et Snapchat Ads. Repérez les dépenses inutiles, vérifiez le suivi et repartez avec un plan d’action priorisé.
An independent audit of your ad accounts and measurement. Find wasted spend and get a prioritized fix plan.\tUn audit indépendant de vos comptes publicitaires et de la mesure des résultats. Repérez les dépenses inutiles et obtenez un plan d’action priorisé.
Portrait of Marcos Arteaga\tPortrait de Marcos Arteaga
Marcos Arteaga, back to top\tMarcos Arteaga, retour en haut de page
Marcos Arteaga, homepage\tMarcos Arteaga, page d’accueil
Language\tLangue
Black-and-white portrait of Marcos Arteaga\tPortrait en noir et blanc de Marcos Arteaga
Organizations represented in Marcos's experience\tOrganisations faisant partie de l’expérience de Marcos
https://yourcompany.com\thttps://votreentreprise.com
What feels off? What have you tried?\tQu’est-ce qui ne va pas? Qu’avez-vous déjà essayé?
How Marcos Arteaga handles audit enquiries, account access, and your personal information.\tComment Marcos Arteaga traite les demandes d’audit, les accès aux comptes et vos renseignements personnels.
How I handle audit enquiries and your personal information.\tComment je traite les demandes d’audit et vos renseignements personnels.
""")

SCHEMA = {
    "name": "Audit de comptes publicitaires",
    "serviceType": "Audit de comptes publicitaires",
    "description": "Audits indépendants à portée fixe de Google Ads, Meta Ads, TikTok Ads et Snapchat Ads, avec rapport écrit, plan d’action priorisé et présentation en direct.",
}
