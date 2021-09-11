Scenario: Click button to start
    Given I have started the app
    When I click on the button 'Click me'
    Then the text 'Hello World' will be displayed