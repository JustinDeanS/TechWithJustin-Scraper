from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://techwithjustin.net')

        name = page.query_selector('.text-black.font-staat').inner_text()
        about_me = page.query_selector('.font-ram.text-black-50.py-2').inner_text()
        print(name)
        print(about_me)

        skills = page.query_selector_all('.col-sm-6.pl-4 > p')

        achievements = page.query_selector_all('.w-100')

        projects = page.query_selector_all('.card-body > .card-title')
        
        print("Skills:")

        for skill in skills:
            print(skill.inner_text())

        print("Achievements:")

        for achievement in achievements:
            print(achievement.inner_text())

        print("Projects:")
        
        for project in projects:
            print(project.inner_text())

        browser.close()

if __name__ == '__main__':
    main()

