"""Reviewed Spain Spanish copy for the audit and privacy pages."""

def pairs(data: str) -> dict[str, str]:
    return dict(line.split('\t', 1) for line in data.strip().splitlines())

TEXT = pairs("""
Marcos Arteaga | Independent Paid Media Audits\tMarcos Arteaga | Auditorías independientes de publicidad digital
Privacy Policy | Marcos Arteaga\tPolítica de privacidad | Marcos Arteaga
Skip to content\tIr al contenido
Book the audit\tSolicitar una auditoría
Paid-media audits · Google · Meta · TikTok · Snapchat\tAuditorías publicitarias · Google · Meta · TikTok · Snapchat
Your ad account is leaking money. I’ll show you exactly where.\tTu cuenta publicitaria está perdiendo dinero. Te enseñaré dónde.
A fixed-scope audit of your Google Ads, Meta Ads, TikTok Ads, or Snapchat Ads accounts, delivered in 10 business days. Every finding backed by your own data. No retainer. No fluff.\tUna auditoría de alcance cerrado de tus cuentas de Google Ads, Meta Ads, TikTok Ads o Snapchat Ads, entregada en 10 días laborables. Cada hallazgo respaldado por tus datos. Sin cuota mensual. Sin rodeos.
Independent diagnosis\tDiagnóstico independiente
Prioritized next steps\tAcciones por orden de prioridad
Personally by Marcos\tHecho personalmente por Marcos
The audit\tLa auditoría
Not a checklist.\tNo es una lista de comprobación.
A diagnosis.\tEs un diagnóstico.
I look for the decisions, settings, and measurement gaps that cost you money. Then I tell you what deserves attention.\tBusco las decisiones, ajustes y fallos de medición que te cuestan dinero. Después te digo qué merece atención.
Structure review\tRevisión de la estructura
Campaigns, budgets, bidding. Is the account built to learn, or built to leak?\tCampañas, presupuestos y pujas. ¿La cuenta está organizada para aprender o para perder dinero?
Waste hunt\tDetección de gasto inútil
Search terms, placements, audience overlap, location and device bleed, and broken negatives. Findings come with evidence from your data.\tTérminos de búsqueda, ubicaciones, solapamiento de audiencias, fugas por zona y dispositivo, y palabras clave negativas mal configuradas. Cada hallazgo se apoya en tus datos.
Tracking check\tRevisión de la medición
Conversion setup and attribution. Can you trust the numbers you’re optimizing toward?\tConfiguración de conversiones y atribución. ¿Puedes fiarte de las cifras que guían tus decisiones?
Message check\tRevisión del mensaje
Does the ad promise match the landing page? A focused review, not creative production.\t¿Cumple la página de destino lo que promete el anuncio? Una revisión concreta, no producción creativa.
The call\tLa decisión
A prioritized fix list: do this week, do this month, leave alone. Prioritization is the product.\tUna lista de cambios por prioridad: esta semana, este mes o mejor dejarlo como está. El valor está en decidir el orden.
What you get\tQué recibes
A written report backed by your account data. A prioritized action plan. A 60-minute walkthrough where I defend every line.\tUn informe escrito basado en los datos de tu cuenta. Un plan de acción por prioridades. Una reunión de 60 minutos en la que explico y defiendo cada recomendación.
The business numbers:\tLos números reales del negocio:
MER from actual sales and the ad spend in scope; paid CAC from spend and new-customer counts. ROAS checked against sales records, not just platform-attributed numbers, with attribution limits called out.\tMER calculado con las ventas reales y la inversión publicitaria analizada; CAC de pago a partir del gasto y los nuevos clientes. ROAS contrastado con las ventas, no solo con las conversiones atribuidas por las plataformas, explicando los límites de atribución.
10 business days from kickoff and access.\t10 días laborables desde la reunión inicial y la entrega de accesos.
Read-only access and kickoff → analysis → report and walkthrough. If I need longer, you’ll hear about it before, not after.\tAcceso de solo lectura y reunión inicial → análisis → informe y presentación. Si necesito más tiempo, te lo diré antes, no después.
The fit\tPara quién es
A clear answer.\tUna respuesta clara.
A clear boundary.\tUn alcance claro.
This is for you if\tEsto es para ti si
You spend at least $5,000 a month across Google Ads, Meta Ads, TikTok Ads, or Snapchat Ads.\tInviertes al menos 5.000 € al mes en Google Ads, Meta Ads, TikTok Ads o Snapchat Ads.
You suspect the account underperforms but nobody can say exactly why.\tSospechas que la cuenta rinde menos de lo que podría, pero nadie sabe decirte por qué.
You want an independent read from someone who does not manage your account.\tQuieres una opinión independiente de alguien que no gestiona tu cuenta.
It isn’t for you if\tEsto no es para ti si
Your monthly ad spend is below roughly $5,000. The economics usually don’t work.\tTu inversión publicitaria mensual está por debajo de unos 5.000 €. Normalmente, los números no compensan.
You want ongoing account management or creative production.\tBuscas gestión continua de la cuenta o producción creativa.
You only want an automated checklist.\tSolo quieres una lista de comprobación automática.
The boundary:\tEl límite:
I don’t operate accounts myself. That keeps the diagnosis independent. Your team can run the fixes from my roadmap, or a vetted partner agency can implement them under a separate engagement quoted after the audit. The audit includes no ongoing management, creative production, or guaranteed ROAS lift.\tYo no gestiono las cuentas. Así mantengo el diagnóstico independiente. Tu equipo puede aplicar los cambios siguiendo mi hoja de ruta, o una agencia colaboradora seleccionada puede hacerlo en un encargo aparte, presupuestado después de la auditoría. La auditoría no incluye gestión continua, producción creativa ni garantías de mejora del ROAS.
How I think\tCómo pienso
Where the leaks come from.\tDe dónde salen las pérdidas.
Three illustrative scenarios, not client results. The actual call comes from your account data.\tTres ejemplos ficticios, no resultados de clientes. Las decisiones reales salen de los datos de tu cuenta.
Tracking\tMedición
What I see\tLo que veo
Platform-reported conversions drive every decision. A purchase event fires twice, and nobody has checked it against actual sales.\tTodas las decisiones se toman según las conversiones de la plataforma. Un evento de compra se registra dos veces y nadie lo ha contrastado con las ventas reales.
Reconcile platform conversions with sales records. Fix measurement, then optimize.\tContrastar las conversiones de la plataforma con las ventas. Corregir la medición y después optimizar.
Why it matters\tPor qué importa
The problem isn’t “ROAS dropped.” It’s steering by a number you can’t trust.\tEl problema no es que «haya bajado el ROAS». Es tomar decisiones con una cifra en la que no puedes confiar.
Incrementality\tIncrementalidad
Prospecting campaigns keep reaching people who already bought. The report counts returning buyers as new demand.\tLas campañas de captación siguen llegando a personas que ya compraron. El informe cuenta a esos compradores recurrentes como demanda nueva.
Exclude known buyers where the platform allows. Separate brand demand from prospecting, with a distinct budget and objective for each.\tExcluir a los compradores conocidos cuando la plataforma lo permita. Separar la demanda de marca de la captación, con presupuesto y objetivo propios para cada una.
The problem isn’t just rising CPA. It’s paying to claim customers you already had.\tEl problema no es solo que suba el CPA. Es pagar por atribuirte clientes que ya tenías.
Feed\tCatálogo
In a Shopping account, products are disapproved or miscategorized. Best sellers barely serve.\tEn una cuenta de Shopping, hay productos rechazados o mal categorizados. Los más vendidos apenas aparecen.
Fix titles, categories, and availability in the product feed before increasing Shopping spend.\tCorregir títulos, categorías y disponibilidad en el feed de productos antes de aumentar la inversión en Shopping.
The problem isn’t “Shopping doesn’t work for us.” The feed is the ad—and yours is broken.\tEl problema no es que «Shopping no nos funcione». El feed es el anuncio, y el tuyo falla.
Independent judgment\tCriterio independiente
Google’s AI works for Google.\tLa IA de Google trabaja para Google.
Automated recommendations can flag settings. They can’t own your tradeoffs or defend which fix comes first. I read the account, the measurement, and the path to conversion. Then I make the call: what to fix now, what can wait, and what to leave alone.\tLas recomendaciones automáticas pueden señalar ajustes. No pueden asumir tus prioridades ni defender qué cambio debe ir primero. Examino la cuenta, la medición y el camino hasta la conversión. Después decido qué corregir ahora, qué puede esperar y qué conviene dejar en paz.
And the chatbots can’t do this either.\tY los chatbots tampoco pueden hacer esto.
Without a direct connection, ChatGPT and Claude can only read what you hand them—screenshots and exports that may miss the path from spend to conversion. I get read-only access to your ad accounts and analytics, make the priority call, and defend it on a live 60-minute call. And pasting your business’s numbers into a chatbot is a data-sharing decision you shouldn’t make lightly.\tSin una conexión directa, ChatGPT y Claude solo pueden leer lo que les pasas: capturas y exportaciones que pueden perder el recorrido entre el gasto y la conversión. Accedo a tus cuentas publicitarias y a tus datos analíticos en modo de solo lectura, decido las prioridades y defiendo esa decisión en una llamada de 60 minutos. Copiar las cifras de tu negocio en un chatbot también es una decisión sobre tus datos que conviene pensar bien.
About Marcos\tSobre Marcos
A specialist,\tUn especialista,
not another dashboard.\tno otro panel de control.
I’m Marcos Arteaga. I’ve worked across fashion retail, DTC, SaaS, B2B, and publishing. I now focus on one job: finding where paid media accounts leak money and giving you a plan you can actually use.\tSoy Marcos Arteaga. He trabajado en moda, venta directa al consumidor, SaaS, B2B y medios digitales. Ahora me centro en una sola tarea: encontrar dónde pierden dinero las cuentas publicitarias y darte un plan que puedas poner en práctica.
Selected experience\tExperiencia seleccionada
Questions\tPreguntas
Before you book.\tAntes de solicitarla.
How is this different from my agency’s audit?\t¿En qué se diferencia de la auditoría de mi agencia?
Your agency has to evaluate work it already owns. I don’t run your account, so I have nothing to defend. You get an independent diagnosis.\tTu agencia tiene que evaluar un trabajo que ya es suyo. Yo no gestiono tu cuenta, así que no tengo nada que defender. Recibes un diagnóstico independiente.
What do you need from me?\t¿Qué necesitas de mí?
Read-only access to your ad accounts, analytics, and sales data (Shopify or equivalent). Nothing gets changed. We start with a 20-minute kickoff call.\tAcceso de solo lectura a tus cuentas publicitarias, analítica y datos de ventas (Shopify o similar). No se cambia nada. Empezamos con una llamada de 20 minutos.
What if you find nothing major?\t¿Y si no encuentras nada importante?
Then I’ll say so. You’ll see what I checked, what held up, and what I’d leave alone. I won’t invent a problem to fill a report.\tTe lo diré. Verás qué he revisado, qué funciona y qué dejaría como está. No inventaré un problema para llenar un informe.
Do you implement the fixes?\t¿Aplicáis los cambios?
Yes, through a vetted partner agency. They can implement from my audit roadmap under a separate engagement, quoted after the audit. Your team can also run the plan. I stay out of the account so the diagnosis stays independent.\tSí, a través de una agencia colaboradora seleccionada. Puede aplicar los cambios de mi hoja de ruta en un encargo aparte, presupuestado después de la auditoría. Tu equipo también puede ejecutar el plan. Yo no entro a gestionar la cuenta para mantener el diagnóstico independiente.
Why a flat fee instead of hourly?\t¿Por qué un precio cerrado y no por horas?
Because you’re buying the answer, not my time. The scope and fee are agreed privately before the audit begins.\tPorque compras una respuesta, no mis horas. El alcance y el precio se acuerdan en privado antes de empezar.
The next step\tEl siguiente paso
Book the audit.\tSolicita una auditoría.
Tell me what’s happening in the account. I’ll reply personally within 2 business days about fit and next steps.\tCuéntame qué pasa en la cuenta. Te responderé personalmente en un plazo de 2 días laborables para hablar de si encaja y de los siguientes pasos.
No account access needed to send an enquiry. If we work together, access is read-only.\tNo necesitas dar acceso a la cuenta para escribir. Si trabajamos juntos, el acceso será de solo lectura.
Fixed scope. Flat fee. No ongoing management.\tAlcance cerrado. Precio fijo. Sin gestión continua.
Name\tNombre
Email\tCorreo electrónico
Website\tSitio web
Monthly ad spend\tInversión publicitaria mensual
Select a range\tElige un tramo
Under $5,000/month\tMenos de 5.000 €/mes
$5,000–$15,000/month\tDe 5.000 a 15.000 €/mes
$15,000–$50,000/month\tDe 15.000 a 50.000 €/mes
$50,000+/month\t50.000 € o más/mes
Platforms\tPlataformas
Choose all that apply.\tMarca todas las que correspondan.
Other platform (ask about fit)\tOtra plataforma (consúltame)
Which other platform?\t¿Qué otra plataforma?
The audit is designed for accounts spending at least $5,000 a month. You can still send a note; I’ll give you an honest answer about fit.\tLa auditoría está pensada para cuentas que invierten al menos 5.000 € al mes. Aun así, puedes escribirme; te diré con sinceridad si tiene sentido para ti.
What’s bothering you about your account?\t¿Qué te preocupa de tu cuenta?
Leave this field blank\tDeja este campo en blanco
I’ll use these details to reply about your audit enquiry.\tUsaré estos datos para responder a tu solicitud de auditoría.
How I handle your information\tCómo trato tus datos
Send audit enquiry\tEnviar solicitud de auditoría
Enquiry sent\tSolicitud enviada
Thanks for reaching out.\tGracias por escribirme.
I’ll reply personally within 2 business days about fit and next steps.\tTe responderé personalmente en un plazo de 2 días laborables para hablar de si encaja y de los siguientes pasos.
Privacy\tPrivacidad
Blog\tBlog (EN)
The plain version\tEn pocas palabras
Privacy policy.\tPolítica de privacidad.
Last updated: October 2026\tÚltima actualización: octubre de 2026
You send an audit enquiry. I use it to answer you. Here’s what happens to the information you share.\tEnvías una solicitud de auditoría. Uso tus datos para responderte. Esto es lo que ocurre con la información que compartes.
What I collect\tQué recojo
When you send an audit enquiry, I collect what you type into the form: your name, email address, website, monthly ad spend range, the platforms you use, and your message. If you choose “Other platform,” I collect the platform you name. No account access is needed—or asked for—at the enquiry stage.\tCuando envías una solicitud de auditoría, recojo lo que escribes en el formulario: nombre, correo electrónico, sitio web, tramo de inversión publicitaria mensual, plataformas que utilizas y mensaje. Si eliges «Otra plataforma», también recojo el nombre que indiques. En esta fase no necesito ni solicito acceso a tus cuentas.
The web host may log standard request details, such as your IP address. To limit spam, the form keeps a hashed IP key and submission times in a server temporary file.\tEl proveedor de alojamiento puede registrar datos técnicos habituales de la solicitud, como tu dirección IP. Para limitar el spam, el formulario guarda un identificador derivado de la IP y las horas de envío en un archivo temporal del servidor.
Why I collect it\tPara qué lo recojo
To reply to your enquiry about fit and next steps. That’s the purpose. The form sends a short automatic acknowledgement; I follow up personally. The technical details keep the form running and limit spam.\tPara responder a tu consulta sobre si la auditoría encaja y cuáles son los siguientes pasos. Ese es el fin. El formulario envía un breve acuse de recibo automático y después te respondo personalmente. Los datos técnicos mantienen el formulario en funcionamiento y ayudan a limitar el spam.
What I don’t do\tQué no hago
I don’t add you to any marketing or newsletter list. I don’t sell or rent your information. I use what you type only to respond to your enquiry. I don’t pass it to a partner agency unless you choose a separate implementation engagement.\tNo te añado a ninguna lista comercial ni boletín. No vendo ni alquilo tus datos. Uso lo que escribes solo para responder a tu consulta. No se lo facilito a una agencia colaboradora salvo que elijas un encargo independiente de implementación.
Where it goes\tDónde van tus datos
Enquiries are emailed to me at\tLas solicitudes me llegan por correo a
through Google Workspace. The site runs on a Plesk web host. Both providers process information needed to run the site and deliver the email; their systems may process it outside Québec.\ta través de Google Workspace. El sitio funciona en un servidor Plesk. Ambos proveedores tratan la información necesaria para alojar el sitio y entregar el correo; sus sistemas pueden tratarla fuera de Québec y de la Unión Europea.
If we end up working together, the audit itself runs on read-only access to your ad accounts, analytics, and sales data. Nothing gets changed, and your data stays yours.\tSi terminamos trabajando juntos, la auditoría utiliza acceso de solo lectura a tus cuentas publicitarias, analítica y datos de ventas. No se modifica nada y tus datos siguen siendo tuyos.
How long I keep it\tCuánto tiempo lo conservo
If we don’t work together, I delete enquiry details within 12 months. If we do, they’re kept for the duration of our working relationship, and longer only if the law requires it. The host’s technical logs and the form’s spam-control records are kept separately for site operation and security.\tSi no trabajamos juntos, elimino los datos de la consulta en un plazo de 12 meses. Si lo hacemos, los conservo mientras dure nuestra relación y durante más tiempo solo si la ley lo exige. Los registros técnicos del alojamiento y los datos antispam del formulario se conservan por separado para el funcionamiento y la seguridad del sitio.
Your rights\tTus derechos
Under Québec’s Law 25, you can ask to see or correct your personal information, withdraw consent where applicable, or ask me to delete it. Legal retention requirements may limit deletion. Email\tSegún la Ley 25 de Québec, puedes solicitar acceso a tus datos personales o su rectificación, retirar tu consentimiento cuando corresponda o pedirme que los elimine. Si estás en la UE, también puedes ejercer los derechos reconocidos por el RGPD y presentar una reclamación ante tu autoridad de protección de datos. Las obligaciones legales de conservación pueden limitar la eliminación. Escribe a
and I’ll handle it personally.\ty me ocuparé personalmente.
Privacy officer\tResponsable de privacidad
Home\tInicio
""")

ATTRS = pairs("""
Independent audits of Google, Meta, TikTok, and Snapchat Ads. Find wasted spend, check tracking, and leave with a prioritized fix plan.\tAuditorías independientes de Google, Meta, TikTok y Snapchat Ads. Detecta gasto inútil, revisa la medición y consigue un plan de acción por prioridades.
An independent audit of your ad accounts and measurement. Find wasted spend and get a prioritized fix plan.\tUna auditoría independiente de tus cuentas publicitarias y medición. Detecta gasto inútil y consigue un plan de acción por prioridades.
Portrait of Marcos Arteaga\tRetrato de Marcos Arteaga
Marcos Arteaga, back to top\tMarcos Arteaga, volver arriba
Marcos Arteaga, homepage\tMarcos Arteaga, página de inicio
Language\tIdioma
Black-and-white portrait of Marcos Arteaga\tRetrato en blanco y negro de Marcos Arteaga
Organizations represented in Marcos's experience\tOrganizaciones presentes en la trayectoria de Marcos
https://yourcompany.com\thttps://tuempresa.com
What feels off? What have you tried?\t¿Qué falla? ¿Qué has intentado ya?
How Marcos Arteaga handles audit enquiries, account access, and your personal information.\tCómo trata Marcos Arteaga las solicitudes de auditoría, el acceso a las cuentas y tus datos personales.
How I handle audit enquiries and your personal information.\tCómo trato las solicitudes de auditoría y tus datos personales.
""")

SCHEMA = {
    "name": "Auditoría de cuentas publicitarias",
    "serviceType": "Auditoría de cuentas publicitarias",
    "description": "Auditorías independientes de alcance cerrado de Google Ads, Meta Ads, TikTok Ads y Snapchat Ads, con informe escrito, plan de acción por prioridades y presentación en directo.",
}
