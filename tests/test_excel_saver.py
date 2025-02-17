from src.ExcelSaver import ExcelSaver


def test_save_to_file(tmp_path, some_list_of_vacancies) -> None:
    """ Тест на сохранение файла формата excel. """
    file_name = tmp_path / 'test'
    saver = ExcelSaver()
    saver.save_to_file(some_list_of_vacancies, str(file_name))

    saver = ExcelSaver()
    saver.save_to_file(some_list_of_vacancies, str(file_name))

    output_file = file_name.with_suffix('.xlsx')
    assert output_file.exists()
