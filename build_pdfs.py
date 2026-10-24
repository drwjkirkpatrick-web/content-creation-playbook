#!/usr/bin/env python3
"""Generate LaTeX sources for the Content Creation Playbook PDFs and compile them.

Content curated from web research (October 2026); source URLs are embedded in
each PDF's Sources section. Re-run to regenerate: python3 build_pdfs.py
"""
import os
import shutil
import subprocess
import sys

OUT_TEX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tex")
OUT_PDF = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pdf")

ACCENT = "0F766E"       # teal
ACCENT2 = "B45309"      # amber
GRAY = "4B5563"

PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[margin=2.2cm,top=2.6cm,bottom=2.4cm]{geometry}
\usepackage[dvipsnames]{xcolor}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage{booktabs}
\usepackage{tcolorbox}
\usepackage{amssymb}
\usepackage{microtype}
\usepackage[colorlinks=true,urlcolor=MidnightBlue,linkcolor=MidnightBlue]{hyperref}
\usepackage{xurl}

\definecolor{accent}{HTML}{0F766E}
\definecolor{accent2}{HTML}{B45309}
\definecolor{softgray}{HTML}{6B7280}

\titleformat{\section}{\Large\bfseries\color{accent}}{\thesection.}{0.6em}{}
\titleformat{\subsection}{\large\bfseries\color{accent2}}{\thesubsection}{0.6em}{}
\titlespacing*{\section}{0pt}{14pt}{6pt}
\titlespacing*{\subsection}{0pt}{10pt}{4pt}

\setlist[itemize]{leftmargin=1.6em,itemsep=5pt,parsep=0pt}
\newcommand{\tip}[2]{\item \textbf{#1.}\enspace #2}
\newcommand{\tlabel}{\textcolor{accent}{\small$\blacktriangleright$}}

\newcommand{\footertitle}{Content Creation Playbook}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[L]{\small\color{softgray}\footertitle}
\fancyfoot[R]{\small\color{softgray}\thepage}

\newcommand{\docbanner}[3]{%
  \begin{center}
    {\color{accent}\rule{\textwidth}{1.4pt}}\\[10pt]
    {\Huge\bfseries\color{black} #1}\\[8pt]
    {\large\color{softgray} #2}\\[8pt]
    {\small\color{softgray} #3}\\[6pt]
    {\color{accent}\rule{\textwidth}{1.4pt}}
  \end{center}
  \vspace{6pt}
}
""".replace("__ACCENT__", "")


def esc(s: str) -> str:
    for ch, rep in (("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"),
                    ("_", r"\_"), ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}")):
        s = s.replace(ch, rep)
    return s


def emit_doc(doc: dict) -> str:
    body = [PREAMBLE, "\\begin{document}\n"]
    body.append("\\hypersetup{pdftitle={%s},pdfsubject={%s},"
                "pdfauthor={drwjkirkpatrick-web},"
                "pdfkeywords={content creation, playbook, %s}}\n" % (
        esc(doc["title"]), esc(doc["subtitle"]), doc["file"].split("-", 1)[-1].replace("-", ", ")))
    body.append("\\renewcommand{\\footertitle}{%s}\n" % esc(doc["title"]))
    body.append("\\docbanner{%s}{%s}{%s}\n" % (
        esc(doc["title"]), esc(doc["subtitle"]), esc(doc["banner"])))
    if doc.get("intro"):
        body.append("\\begin{tcolorbox}[colback=accent!5,colframe=accent,boxrule=0.8pt,"
                    "arc=2pt,left=8pt,right=8pt,top=6pt,bottom=6pt]\n"
                    "\\small " + esc(doc["intro"]) + "\n\\end{tcolorbox}\n\\vspace{6pt}\n")
    num = 0
    for group, tips in doc["groups"]:
        body.append("\\section*{%s}\n" % esc(group))
        body.append("\\begin{itemize}[label=\\tlabel]\n")
        for t, d in tips:
            num += 1
            body.append("\\tip{%d. %s}{%s}\n" % (num, esc(t), esc(d)))
        body.append("\\end{itemize}\n")
    if doc.get("sources"):
        body.append("\\section*{Sources}\n\\begin{itemize}[label={},leftmargin=0.9em,"
                    "itemsep=1pt]\n\\footnotesize\n")
        for label, url in doc["sources"]:
            body.append("\\item \\href{%s}{%s} \\\\ {\\color{softgray}\\url{%s}}\n"
                        % (url, esc(label), url))
        body.append("\\end{itemize}\n\\normalsize\n")
    body.append("\\end{document}\n")
    return "".join(body)


MASTER = {
    "file": "00-master-50-ways",
    "title": "50 Ways to Improve Your Content Creation",
    "subtitle": "The cross-cutting playbook",
    "banner": "Compiled from web research across creator guides, platform data, and craft manuals - October 2026",
    "intro": "These 50 moves apply to every content type. Each is one sentence you can act on today; "
             "the companion PDFs in this repo adapt them per medium. Change one variable at a time, "
             "measure weekly, and keep what survives contact with your audience.",
    "groups": [
        ("Strategy and Positioning", [
            ("Niche down to one sentence", "Define who you help, what problem you solve, and why your answer is different - then put it in your bio, pinned post, or channel header."),
            ("Pick 3-5 content pillars", "Every post should ladder up to a pillar; pillars give your calendar structure and your audience a reason to subscribe."),
            ("Hyper-specify your audience", "'Physicians curious about AI' beats 'people interested in tech' - specificity is what makes content feel personal."),
            ("Study the competition weekly", "Steal structures and formats that demonstrably work; never steal substance."),
            ("Write the title before the content", "If the promise isn't worth a title, the content isn't worth making."),
            ("Give every piece one measurable goal", "Views, saves, replies, or conversions - pick one and judge the piece by it."),
            ("Keep a running idea backlog", "Mine your comments, inbox, and daily questions; the backlog kills the blank page."),
        ]),
        ("Craft and Storytelling", [
            ("Lead with the hook, context second", "The single most interesting thing goes in the first 5-10 seconds; context is earned after attention is granted."),
            ("Front-load the payoff", "Deliver the core answer or insight within the first 25-40% of the piece, then deepen it."),
            ("Open a loop every 60-90 seconds", "Tease what's coming, ask a question you'll answer later, and close loops deliberately."),
            ("Apply the so-what test", "If deleting a sentence loses the audience nothing, delete it - density is retention."),
            ("Use problem-tension-payoff structure", "Open with a problem, build stakes, end with a clear takeaway the viewer can restate."),
            ("Show proof, don't claim it", "Demonstrate the finished result early instead of promising it verbally."),
            ("Vary pacing on purpose", "Alternate fast and slow segments; rhythm contrast fights cognitive fatigue."),
            ("Distribute micro-payoffs", "Small wins of value throughout beat one big payoff at the end."),
        ]),
        ("Production Quality", [
            ("Fix audio before video", "Clear audio beats sharp footage; listeners forgive soft video, never bad sound."),
            ("Light simply and evenly", "One key light or a window beats a ring of gadgets; flat, even light reads at small sizes."),
            ("Compose with the rule of thirds", "Put the subject near a grid intersection with an uncluttered background."),
            ("Record test clips before full takes", "Check levels, framing, and noise in 30 seconds, not after a 20-minute take."),
            ("Batch your production", "Write in one block, shoot in another, edit in a third - context switching is the silent killer."),
            ("Build a repeatable workflow", "Templates, presets, and checklists turn production from an event into a routine."),
            ("Cut every pause that adds nothing", "Tight editing keeps energy up; dead air is where audiences leave."),
        ]),
        ("Packaging", [
            ("Make the thumbnail or cover one dominant subject", "One focal point at 60%+ of the frame beats three competing ones."),
            ("Limit packaging text to 3-4 words", "Big, bold, high-contrast; text is a supporting actor, not the star."),
            ("Preview packaging at thumbnail size", "If it doesn't read at 120 pixels wide, redesign before publishing."),
            ("Write specific, curiosity-honest titles", "Specific beats clever; the hook must match what the content delivers."),
            ("Keep captions and on-screen text always on", "A large share of viewing is sound-off; captions are retention and accessibility at once."),
            ("Lock a consistent visual brand", "Two or three colors and one font, everywhere, builds recognition compounds."),
        ]),
        ("Distribution and Repurposing", [
            ("Publish on a fixed cadence", "A schedule the audience can rely on outperforms sporadic brilliance."),
            ("Repurpose every long piece into shorts", "One long video becomes 3-5 clips; get more reps without more filming days."),
            ("Optimize per platform, don't blind cross-post", "Adjust length, caption style, and music to each algorithm; strip watermarks."),
            ("Post when your audience is actually online", "Platform insights show you when; timing is free reach."),
            ("Build an email list early", "It's the only audience the algorithm can't take from you."),
            ("Do SEO and AEO basics", "Keywords in titles/descriptions and clear answers to specific questions win search and answer engines."),
            ("Collaborate on purpose", "Guest swaps and duets borrow trust; pick partners your audience already respects."),
        ]),
        ("Engagement and Community", [
            ("Make one clear call to action per piece", "One ask converts; three asks cancel each other out."),
            ("Mine comments for content", "Reader questions are pre-validated topics - answer them publicly."),
            ("Ask questions that invite replies", "End pieces with a question people can answer from experience."),
            ("Feature your audience", "User-generated content and reader spotlights turn viewers into co-creators."),
            ("Reply while the audience is small", "Early reply culture compounds into the community you'll have later."),
        ]),
        ("Analytics and Iteration", [
            ("Review analytics weekly", "A fixed weekly review beats daily doom-scrolling the dashboard."),
            ("Track saves and shares over likes", "Saves and shares predict reach better; likes are applause, saves are intent."),
            ("A/B test hooks, thumbnails, subject lines", "Change one variable, keep the winner, and log the result."),
            ("Read retention curves by timestamp", "Find the exact second audiences leave and fix that moment, not the whole video."),
            ("Kill your bottom third", "Retire the formats and topics in the bottom third of performance every month."),
        ]),
        ("Systems and Sustainability", [
            ("Keep slack in the calendar", "A calendar with room to pivot survives trends and life events; a full one collapses."),
            ("Use AI for structure, verify facts yourself", "AI drafts outlines and speeds iteration; accuracy and voice stay human."),
            ("Maintain a media kit", "Stats, past work, and contact info on one page make opportunities find you."),
            ("Protect the creator, not just the output", "Sustainable routines and scheduled downtime prevent the burnout that kills channels."),
            ("Ship before it's perfect", "Publish, iterate in public, and let version 2 be informed by real data."),
        ]),
    ],
    "sources": [
        ("MySocial - Content Creation: What It Is and How to Scale It", "https://mysocial.io/blog/content-creation/"),
        ("Hootsuite - Social media content creation: 15 pro tips", "https://blog.hootsuite.com/social-media-content-creation/"),
        ("Backstage - 7 Essential Skills Every Content Creator Needs", "https://www.backstage.com/magazine/article/content-creator-skills-79954/"),
        ("Bluehost - How to Become a Content Creator in 2026", "https://www.bluehost.com/blog/how-to-become-a-content-creator/"),
        ("Designrr - Content Marketing Tips", "https://designrr.io/content-marketing-tips/"),
        ("Access Creative - What skills do you need as a content creator?", "https://www.accesscreative.ac.uk/blog/what-skills-do-you-need-as-a-content-creator/"),
    ],
}

VIDEO = {
    "file": "01-video-youtube",
    "title": "Video and YouTube",
    "subtitle": "12 ways to improve long-form video",
    "banner": "Adapted for long-form video and YouTube from retention research and hook-optimization guides",
    "intro": "On YouTube, retention architecture beats production polish. The metrics that matter: "
             "30-second retention (aim 70%+), the retention curve's drop-off timestamps, and click-through rate.",
    "groups": [
        ("The First 30 Seconds", [
            ("Hook within 5-10 seconds", "State the exact outcome the viewer gets; a promise confirmation, pattern interrupt, or immediate payoff."),
            ("Match the hook to the title exactly", "The viewer needs immediate visual and spoken confirmation they're in the right place."),
            ("Show visual proof in under 10 seconds", "Display the finished result before explaining how you got it."),
            ("Cut all preamble", "No logo stings, channel animations, or throat-clearing - be into step one before the 25-second mark."),
            ("Open a curiosity loop before step one", "Plant a seed about the mistake or shortcut coming later, then pay it off."),
        ]),
        ("Holding Attention", [
            ("Front-load value by the 25-40% mark", "Deliver the core answer early; depth and nuance come after the payoff, not before it."),
            ("Interrupt patterns every 30-60 seconds", "B-roll, graphics, angle changes, and cuts re-engage drifting attention."),
            ("Re-hook every 60-90 seconds", "Micro-teasers and open loops at section boundaries stop silent bleed."),
            ("Distribute micro-payoffs", "Small wins of value throughout the video, not one payoff at the end."),
            ("Make the viewer the protagonist", "Use 'you' over 'I'; every section should be a step toward the question the video answers."),
        ]),
        ("Structure and Iteration", [
            ("Add timestamped chapters", "Navigability is retention; let viewers self-select without leaving."),
            ("Film two hooks and compare", "Publish the stronger opening, check retention at 48 hours, and reuse the loser later."),
            ("End with one specific next action", "A single end-screen target beats a menu of options."),
        ]),
    ],
    "sources": [
        ("TubeAnalytics - YouTube Video Structure and Retention Optimization", "https://www.tubeanalytics.net/blog/youtube-video-structure-retention-optimization-guide"),
        ("TubeAnalytics - How to Hook Viewers in the First 30 Seconds", "https://www.tubeanalytics.net/blog/youtube-video-hook-first-30-seconds"),
        ("Crayo - 7 Ways to Write YouTube Hooks That Keep Viewers Watching", "https://crayo.ai/blog/youtube-hooks"),
        ("LTX - Short-Form Video: Strategy, Formats, and AI Creation Guide", "https://ltx.io/blog/short-form-video"),
    ],
}

WRITING = {
    "file": "02-writing-blogging-newsletters",
    "title": "Writing, Blogging, and Newsletters",
    "subtitle": "12 ways to improve the written word",
    "banner": "Adapted for blogs, articles, and email newsletters from engagement and deliverability research",
    "intro": "Written content competes with the scroll and the inbox. Scannability, one-CTA discipline, "
             "and ruthless curation are what separate read from skimmed from deleted.",
    "groups": [
        ("Opening and Structure", [
            ("Write the headline or subject line first", "Specific and curiosity-honest beats clever or clickbaity; the promise sets the article's contract."),
            ("Hook the preview text", "The first sentence of an email shows in the inbox - write it as if the delete button is next to it."),
            ("Keep paragraphs to 2-3 sentences", "Subheadings, bullets, bold key phrases, and white space respect the reader's time."),
            ("Stay under 300-500 words for email", "Newsletters link out to depth; they don't reproduce it."),
        ]),
        ("Substance and Voice", [
            ("Use concrete details over generic claims", "Specific numbers, names, and moments are what readers remember and repeat."),
            ("Include failures with the wins", "Vulnerability builds trust; connect individual stories to universal experiences."),
            ("Bold every unclear term and link it", "If a reader might not know a concept, hyperlink the explanation inline."),
            ("Curate ruthlessly", "Deep insight on two topics beats surface coverage of ten."),
        ]),
        ("Conversion and Cadence", [
            ("One primary CTA per piece", "Make secondary actions hypertext, not buttons; the ask must fit the content's natural conclusion."),
            ("Segment your list", "By interest, engagement level, or journey stage - then tailor subject lines and intros to each group."),
            ("A/B test subject lines and placements", "Test one element at a time; you were sending something either way."),
            ("Draft ahead on a fixed schedule", "Never send just to hit the calendar; send only when you have something worth the reader's attention."),
        ]),
    ],
    "sources": [
        ("AWeber - How to Write a Newsletter That Makes You Unforgettable", "https://blog.aweber.com/learn/how-to-write-a-newsletter.htm"),
        ("beehiiv - 8 Tactics for Building a Highly Engaged Newsletter", "https://www.beehiiv.com/blog/8-ways-build-engaged-newsletter"),
        ("Fast Company - 18 tips to keep your newsletter fresh", "https://www.fastcompany.com/91228587/biz-blogging-101-18-tips-to-keep-your-newsletter-fresh-and-exciting"),
        ("Brafton - 9 Newsletter Engagement Strategies That Work", "https://www.brafton.com/blog/email-marketing/newsletter-engagement-strategies/"),
        ("Inside News - How to Keep Your Newsletter Audience Engaged", "https://insidenews.co.uk/how-to-keep-your-newsletter-audience-engaged/"),
        ("Kate the (Almost) Great - Why You Need a Blog Newsletter", "https://katethealmostgreat.com/why-you-need-a-blog-newsletter/"),
    ],
}

PODCAST = {
    "file": "03-podcasting-audio",
    "title": "Podcasting and Audio",
    "subtitle": "12 ways to improve your show",
    "banner": "Adapted for podcasts from recording, editing, and interviewing best-practice guides",
    "intro": "Audio is the most forgiving medium in production and the least forgiving in quality: "
             "listeners tolerate mediocre content longer than they tolerate bad sound. Fix the room and "
             "the mic first, then the structure, then the polish.",
    "groups": [
        ("Recording", [
            ("Record in a soft, quiet room", "Rugs, curtains, and closets full of clothes absorb echoes; hard reflective rooms are the top audio killer."),
            ("Mic 4-6 inches away, slightly off-axis", "Angle the mic 15-30 degrees off-center and add a pop filter to tame plosives."),
            ("Always wear headphones", "They prevent remote-guest echo and let you catch plosives and breath noise live."),
            ("Record separate tracks per speaker", "The decision pays for itself the first time you edit a crossover conversation."),
            ("Mute yourself when others speak", "'Mm-hmm' interruptions are annoying to hear and miserable to edit out."),
            ("Record a test clip first", "Thirty seconds of playback beats an hour of unfixable noise."),
        ]),
        ("Structure", [
            ("Cold-open with the best moment", "Preview the strongest 15-30 seconds before the intro."),
            ("Keep the intro under 60 seconds", "Branding, host name, and topic framing - then get out of the way."),
            ("Re-order for narrative, not chronology", "Move the strongest answer earlier; the conversation doesn't have to play in recorded order."),
            ("Ask open-ended, researched questions", "Study the guest's work; ask for stories, not yes/no answers."),
        ]),
        ("Editing", [
            ("Content edit before technical processing", "Tighten structure first - EQ on audio you're about to cut is wasted work."),
            ("Trim the runway before good answers", "Cut dead starts and framing that buries the question; target -16 LUFS for stereo."),
        ]),
    ],
    "sources": [
        ("OBSBOT - 30 Essential Podcast Tips", "https://www.obsbot.com/blog/podcast/podcast-tips"),
        ("Podmuse - How to Edit Audio for Podcast: A Pro Workflow", "https://www.podmuse.com/post/edit-audio-for-podcast"),
        ("Descript - Podcast Tips: Practical Ways to Improve Your Show", "https://www.descript.com/blog/article/podcast-tips"),
        ("Fame - Top Podcast Best Practices To Grow Your Show", "https://www.fame.so/post/podcast-best-practices"),
        ("Hollyland - How to Start a Successful Podcast", "https://store.hollyland.com/blogs/creator-hub/start-a-successful-podcast"),
        ("The Podcast Consultant - How to Host Good Podcast Interviews", "https://thepodcastconsultant.com/blog/how-to-host-good-podcasts"),
    ],
}

SOCIAL = {
    "file": "04-social-short-form",
    "title": "Social and Short-Form Video",
    "subtitle": "12 ways to improve TikTok, Reels, and Shorts",
    "banner": "Adapted for TikTok, Instagram Reels, and YouTube Shorts from 2026 platform-data guides",
    "intro": "Short-form is a hook economy: the first 3 seconds drive most of the completion variance, "
             "and completion plus saves - not likes - drive reach. Cadence and format repeatability beat "
             "one-off virality.",
    "groups": [
        ("The Hook", [
            ("Hook in the first 2-3 seconds", "Bold visual, surprising object, or direct address - the swipe decision happens immediately."),
            ("Write 20 hooks before filming", "Spend ten minutes on hook variants for one topic; treat hooks as data, not taste."),
            ("Design the first frame visually", "The frame must work with sound off: bold text, expressive face, or unusual context."),
            ("Script three beats: hook, proof, payoff", "Hook 0-3s, proof 3-30s, payoff/CTA in the last 5s."),
        ]),
        ("Format and Platform", [
            ("Optimize completion, not duration", "A 45-second video with 70% completion beats a 15-second with 40%; cut to the payoff, not a target length."),
            ("Use 1-3 hashtags, mixed broad and niche", "One trending, one community, one descriptive - the algorithm punishes obvious bait."),
            ("Say your keywords out loud", "Speech recognition feeds content classification; captions should echo search phrases."),
            ("Remove watermarks when repurposing", "Cross-post the same 9:16 file, but strip TikTok marks before Reels or Shorts."),
            ("Pick formats, not trends", "Challenges, comedy, reactions, and POV explainers keep earning; pick the format before the topic."),
        ]),
        ("Cadence and Iteration", [
            ("Post 3-7 times per week", "Daily cadence for the first 90 days builds the niche signal; consistency beats weekly excellence."),
            ("Batch film 5-10 videos per session", "Set up once, record while in position, schedule across the week."),
            ("Track saves and kills your bottom third", "Saves are 2-3x more valuable than likes; review first-3-second retention per hook monthly."),
        ]),
    ],
    "sources": [
        ("Digital Applied - Short-Form Video Strategy: Shorts vs TikTok vs Reels", "https://www.digitalapplied.com/blog/short-form-video-strategy-shorts-tiktok-reels-2026"),
        ("Loudscale - How to Master Short-Form Video Marketing in 2026", "https://loudscale.com/guides/master-short-form-video-marketing-2026/"),
        ("Reelsmaker AI - Short-Form Video Strategy 2026 Playbook", "https://reelsmakerai.com/short-form-video-strategy"),
        ("The Social Skinny - Short-Form Video Strategy for 2026", "https://www.thesocialskinny.com/short-form-video-strategy-for-2026-how-to-win-on-tiktok-reels-and-youtube-shorts/"),
        ("Revid - Short Form Video Trends 2026", "https://www.revid.ai/blog/short-form-video-trends"),
        ("Stack Influence - Video Content Optimization 2026", "https://stackinfluence.com/blog/video-content-optimization"),
    ],
}

VISUAL = {
    "file": "05-visual-design-thumbnails",
    "title": "Visual Design and Thumbnails",
    "subtitle": "12 ways to improve images, covers, and thumbnails",
    "banner": "Adapted for thumbnails, social images, and photography from design and click-psychology guides",
    "intro": "Packaging decides whether great content gets seen. Design for the 120-pixel preview: "
             "one dominant subject, high contrast, and minimal text, tested at thumbnail size before publishing.",
    "groups": [
        ("Composition and Light", [
            ("One dominant subject per image", "Everything else supports the focal point; if everything fights equally, nothing wins."),
            ("Place subjects on the rule-of-thirds grid", "Faces near an intersection, not dead center; fill 30-60% of the frame."),
            ("Shoot flat, even light on faces", "Clarity beats drama at small sizes; add shadow in post, fix underexposure never."),
            ("Separate subject from background", "Tonal contrast, a subtle blur, or a subject stroke; keep backgrounds quieter than the subject."),
            ("Use diagonal energy", "Tilted heads and corner-to-corner lines read as movement; static horizontals read as passive."),
            ("Leave breathing room for platform crops", "Vertical-first for social; keep key elements away from edges."),
        ]),
        ("Design Details", [
            ("Limit text to 3-4 bold words", "Heavy-weight font, outlined or shadowed, in the upper third; text is a supporting actor."),
            ("Stick to 2-3 colors", "Complementary pairs (blue/orange, yellow/purple) guide focus; consistency builds brand."),
            ("Push expressions past comfort", "What looks over-the-top live reads natural at thumbnail size; clear eyes win clicks."),
            ("Apply the 3-element rule", "Face, key object, short text - nothing else in the frame."),
        ]),
        ("Testing", [
            ("Preview at 120 pixels before publishing", "If the subject doesn't read on a phone screen, crop tighter or simplify."),
            ("Change one design variable per test", "Composition, lighting, or expression - isolate the cause of the click-rate change."),
        ]),
    ],
    "sources": [
        ("Creator Science - How to Make Great YouTube Thumbnails When You're Not a Designer", "https://www.wisdomai.com/insights/Creator%20Science/youtube-thumbnails-composition-rule-of-thirds-thumbnail-design-6449a1b7"),
        ("Henry David Photography - YouTube Thumbnail Design Guide for 2026", "https://www.henrydavidphotography.com/resources/blog/youtube-thumbnail-design-guide"),
        ("Thumbnail Creator - Ultimate Guide to Thumbnail Composition", "https://www.thumbnailcreator.com/blog/thumbnail-composition-guide"),
        ("Adobe Express - 7 Proven social media photography tips", "https://www.adobe.com/express/learn/blog/social-media-photography-tips"),
        ("Debbie Photos - How to Create Strong Thumbnail Images", "https://www.debbiephotos.com/how-to-create-strong-thumbnail-images/"),
        ("Photoroom - How to make eye-catching YouTube thumbnails", "https://www.photoroom.com/blog/make-youtube-thumbnails"),
    ],
}

DOCS = [MASTER, VIDEO, WRITING, PODCAST, SOCIAL, VISUAL]


def main() -> int:
    os.makedirs(OUT_TEX, exist_ok=True)
    os.makedirs(OUT_PDF, exist_ok=True)
    failed = []
    for doc in DOCS:
        tex = emit_doc(doc)
        tex_path = os.path.join(OUT_TEX, doc["file"] + ".tex")
        with open(tex_path, "w") as f:
            f.write(tex)
        for _ in range(2):  # two passes for hyperref/refs
            r = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                 "-output-directory", OUT_TEX, tex_path],
                capture_output=True, text=True)
            if r.returncode != 0:
                print(f"FAIL {doc['file']}:\n{r.stdout[-1500:]}")
                failed.append(doc["file"])
                break
        else:
            src = os.path.join(OUT_TEX, doc["file"] + ".pdf")
            dst = os.path.join(OUT_PDF, doc["file"] + ".pdf")
            shutil.copy(src, dst)
            print(f"OK   {dst}  ({os.path.getsize(dst)//1024} KB)")
    if failed:
        print(f"\n{len(failed)} failed: {failed}")
        return 1
    total = sum(len(tips) for _, tips in MASTER["groups"])
    print(f"\nMaster list: {total} tips; per-type docs: {len(DOCS)-1}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
