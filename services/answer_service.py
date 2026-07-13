from tools.file_writer import save_answers


class AnswerService:

    @staticmethod
    def save(

        username,

        question,

        assistant,

        research

    ):

        save_answers.run(

            username=username,

            question=question,

            assistant_answer=assistant,

            search_answer=research

        )