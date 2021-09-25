Scenario Outline: Enter name to be welcomed
    Given I have entered the app
    When I enter <my_name> in the input field
    Then the text 'Hello <my_name>' will be displayed

    Examples:
        | my_name |
        | maaeli |
        | マエリ |
        | 마에리 | 