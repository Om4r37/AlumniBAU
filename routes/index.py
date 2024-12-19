from flask import Blueprint, redirect, render_template, session
from utils import login_required

bp = Blueprint("index", __name__)


@bp.route("/")
@login_required
def index():
    return redirect(
        "/survey"
        if session.get("role") == "alumnus"
        else (
            "/stats"
            if "stats" in session.get("perms")
            else (
                "/manage"
                if "manage" in session.get("perms")
                else (
                    "/announce"
                    if "announce" in session.get("perms")
                    else "/mod" if "mod" in session.get("perms") else "/news"
                )
            )
        )
    )


@bp.route("/about")
def about():
    about = {
        "What is Alumni System": "The Alumni System at Al-Balqa Applied University is a vital tool for strengthening the relationship between the university and its graduates, contributing to the growth of both the institution and the personal and professional development of its alumni.",
        "What Alumni Can Do": "Through this system, the university can track and update alumni's personal and professional information, organize career-related events and services, and facilitate connections among graduates and university staff. This enhances alumni networks and provides continuous opportunities for career advancement and professional development.",
        "Alumni and Graduates": "The system empowers graduates by enabling them to expand their professional networks, exchange knowledge, and collaborate with peers on projects or career guidance. It serves as a platform for fostering both personal and professional growth while bridging the gap between academia and the workforce.",
        "Career Opportunities": "Facilitating access to job opportunities, mentorship, and career-related resources, the system ensures that graduates remain connected to their alma mater and benefit from lifelong learning.",
        "Strategic Partnerships": "The Alumni System strengthens the university's ability to form strategic partnerships with local and international organizations, creating pathways for internships, research opportunities, and joint initiatives. These partnerships not only contribute to the community's economy but also elevate the university's reputation in academic, professional, and industrial domains.",
        "Alumni Engagement": "The system acts as a hub for alumni engagement by hosting events, sharing updates, and fostering a sense of belonging. It enables graduates to actively participate in university activities, contribute to decision-making processes, and advocate for future developments.",
    }
    return render_template("about.jinja", about=about)

@bp.route("/jobs")
def jobs():
    class Platform:
        def __init__(self, name, logo, url):
            self.name = name
            self.logo = logo
            self.url = url
    
    platforms = [
        Platform("FORUS.JO", "https://forus.jo/sites/default/files/logofuras.png", "https://forus.jo"),
        Platform("akhtaboot", "https://pbs.twimg.com/profile_images/464341682951966720/EaJ2ZqEO_400x400.png", "https://www.akhtaboot.com"),
        Platform("وزارة العمل", "https://www.mol.gov.jo/ebv4.0/root_storage/ar/eb_homepage/logo-0.png", "https://www.mol.gov.jo"),
        Platform("Bayt", "https://pbs.twimg.com/profile_images/1524327465308598274/nncPN0s8_400x400.jpg", "https://www.bayt.com"),
        Platform("foundit", "https://play-lh.googleusercontent.com/Uw5EnL1NtuH3wdbfOp-SsLuUKtD6bqwlVTBgSn0ULWk3SGbBomauQ1JWvg-0yPBKqQ=w240-h480", "https://www.founditgulf.com"),
        Platform("naukrigulf", "https://play-lh.googleusercontent.com/gfznhMjjzcSoQrMczF7TNQcs5hcCUjV-zl6dz0moN_Er6cRdwUfgSDPFF2a-y-x59w=s64", "https://www.naukrigulf.com"),
        Platform("for9a", "https://www.for9a.com/r-assets/images/Frsa-logo.svg", "https://www.for9a.com/jobs"),
        Platform("wzfni", "https://pbs.twimg.com/profile_images/1268942248202420225/k-pbocty_400x400.jpg", "https://www.wzfni.com"),
        Platform("wadhfny", "https://media.licdn.com/dms/image/v2/C4E0BAQHAGILoetRSwQ/company-logo_200_200/company-logo_200_200/0/1631128705413?e=2147483647&v=beta&t=CQrTriM-amfuQb_wIcOy5Eg1H-9KpqlRK57Mz3oELgg", "https://wadhfny.com"),
        Platform("Laimoon", "https://pbs.twimg.com/profile_images/2986017293/7891045878eaebdb7b2a0d9e47f0851f_400x400.png", "https://jobs.laimoon.com"),
        Platform("LinkedIn", "https://media.licdn.com/dms/image/v2/C560BAQHaVYd13rRz3A/company-logo_200_200/company-logo_200_200/0/1638831590218/linkedin_logo?e=2147483647&v=beta&t=HMVBiFMV-HgYXlCGY6Xk6_d_atqf3B8NDd1lVbfCRlE", "https://www.linkedin.com"),
        Platform("Indeed", "https://avatars.slack-edge.com/2022-06-08/3628164267735_7035d65564bb181b33f7_512.png", "https://www.indeed.com"),
        Platform("Glassdoor", "https://static-00.iconduck.com/assets.00/glassdoor-icon-2048x2048-4di6xoda.png", "https://www.glassdoor.com"),
        Platform("Monster", "https://m.bbb.org/prod/ProfileImages/09144e49-e9c8-414b-9d5c-ed526f60f9b0.png", "https://www.monster.com"),
        Platform("CareerBuilder", "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRyaSZy82JyBJs5ybtYpJTLX5ojNe7pFPqhfKegX-5tgxKA2w6i", "https://www.careerbuilder.com"),
        Platform("SimplyHired", "https://miro.medium.com/v2/resize:fit:2400/1*EOOqxn-vhQeoSvpVmNP-WQ.png", "https://www.simplyhired.com"),
        Platform("ZipRecruiter", "https://www.ziprecruiter.com/apple-touch-icon.png", "https://www.ziprecruiter.com"),
        Platform("Snagajob", "https://images.crunchbase.com/image/upload/c_pad,h_256,w_256,f_auto,q_auto:eco,dpr_1/z8izu8vnptyy66i56jy7", "https://www.snagajob.com"),
        Platform("Job.com", "https://4523910.fs1.hubspotusercontent-na1.net/hubfs/4523910/JOBDOTCOM_Black_green.png", "https://www.job.com"),
        Platform("Jobs2Careers", "https://jobs2-careers.com/wp-content/uploads/2021/08/TSS-icon-gold.png", "https://www.jobs2careers.com"),
        Platform("CareerJet", "https://static.careerjet.org/images/favicon/og-160x160.png?v=2020022501", "https://www.careerjet.com"),
        Platform("JobisJob", "https://is1-ssl.mzstatic.com/image/thumb/Purple71/v4/87/a1/be/87a1bee5-fcf2-3b6e-5bcc-852fd3ec3434/source/512x512bb.jpg", "https://www.jobisjob.com"),
        Platform("JobRapido", "https://img.sur.ly/favicons/a/ae.jobrapido.com.ico", "https://www.jobrapido.com"),
        Platform("JobInventory", "https://pbs.twimg.com/profile_images/499943827663093760/qdJkNMA3_400x400.png", "https://www.jobinventory.com"),
        Platform("Jobcase", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvYWZeP6RHTUuTsK17d4CFwveVBnqSy_HDwQ&s", "https://www.jobcase.com"),
        Platform("JobG8", "https://media.licdn.com/dms/image/v2/C560BAQE1Ih1X5CJ-hg/company-logo_200_200/company-logo_200_200/0/1631329979269?e=2147483647&v=beta&t=bu7QEQTdvMMlKuLfyyooBC3jarPZVVJZXBcJjMsqmbY", "https://www.jobg8.com"),
        Platform("Jobing", "https://logodix.com/logo/1838156.jpg", "https://www.jobing.com"),
        Platform("JobMonkey", "https://media.licdn.com/dms/image/v2/C560BAQEFofSav6CkxQ/company-logo_200_200/company-logo_200_200/0/1644523097523/jobmonkey_inc_logo?e=2147483647&v=beta&t=0PgG9w5bNKpp4IJ8o7_VyetnfDfwSTVs0J_7OvJp9Ag", "https://www.jobmonkey.com"),
        Platform("JobSpider", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWpm6uyxwZIPLqMScB53e5P7_3y2TXPLxqVA&s", "https://www.jobspider.com"),
        Platform("Jobvertise", "https://cdn-b.saashub.com/images/app/service_logos/28/904433117c28/large.png?1548974417", "https://www.jobvertise.com"),
        Platform("Juju", "https://pbs.twimg.com/profile_images/378800000040835807/62e17240585c01245454936f05b42652_400x400.png", "https://www.juju.com"),
        Platform("LinkUp", "https://media.licdn.com/dms/image/v2/D560BAQET9AGbZkBUUA/company-logo_200_200/company-logo_200_200/0/1697467961130/linkup_job_market_data_logo?e=2147483647&v=beta&t=AHTuq7CXw_XscEu_CLdu4iooybyfctXbyI2tlJL0gXQ", "https://www.linkup.com"),
        Platform("Neuvoo", "https://media.licdn.com/dms/image/v2/C4E0BAQE3tbQrZxz6HQ/company-logo_200_200/company-logo_200_200/0/1630596444461/neuvoo_ca_logo?e=2147483647&v=beta&t=xo5a-nhiUq_zIWsVkK2m3nUKzVOQHU4HMx66sjc5hMg", "https://www.neuvoo.com"),
        Platform("Recruit.net", "https://media.licdn.com/dms/image/v2/C4D0BAQF5UHjNAMCSrA/company-logo_200_200/company-logo_200_200/0/1656779867378/recruit_net_logo?e=2147483647&v=beta&t=Tx8TpG2ovfqgdgkIRq3xrhwx-MMPeZTwecl7Xi4qbiU", "https://www.recruit.net"),
        Platform("Workopolis", "https://cdn-1.webcatalog.io/catalog/workopolis/workopolis-icon-unplated.png?v=1714777858742", "https://www.workopolis.com"),
        Platform("WorkSource", "https://tenantconnect.org/wp-content/uploads/2021/09/WorkSource-logo.png", "https://www.worksource.com"),
        Platform("XpatJobs", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTDW6zpiGE0nOfwv5qm9UP7qPAx-5RXd2E-A&s", "https://www.xpatjobs.com"),
        Platform("Yakaz", "https://avatars.githubusercontent.com/u/1457890?s=200&v=4", "https://www.yakaz.com"),
        Platform("Zippia", "https://cdn.freelogovectors.net/wp-content/uploads/2021/11/zippia-logo-freelogovectors.net_.png", "https://www.zippia.com"),
    ]        
    return render_template("jobs.jinja", platforms=platforms)