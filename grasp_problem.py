from requests_html import HTMLSession


def grasp_problem(problem_id: int):
    session = HTMLSession()
    res = session.get(
        "http://10.7.95.2/CLanguage/showproblem?lang=zh&problem_id=%d" % problem_id
    )

    describe: str = res.html.find(
        "#content > div > div:nth-child(4) > p", first=True
    ).text
    input_des: str = res.html.find(
        "#content > div > div:nth-child(6) > p", first=True
    ).text
    output_des: str = res.html.find(
        "#content > div > div:nth-child(8) > p", first=True
    ).text
    sample_output: str = res.html.find(
        "#content > div > div:nth-child(10)", first=True
    ).text
    hint_list_raw: list = res.html.find("#content > div > div:nth-child(12) > p")
    hint_list = []
    for e in hint_list_raw:
        hint_list.append(e.text)

    return {
        "Describe": describe,
        "Input": input_des,
        "Output": output_des,
        "Sample": sample_output,
        "Hints": hint_list,
    }