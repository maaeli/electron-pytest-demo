Scenario: Click button to start
    Given I have started the app
    When I click on the button 'Click me'
    Then the text 'Hello World' will be displayed

Scenario: Click button to start subheading
    Given I have started the app
    When I click on the button 'Click me'
    Then the text 'Welcome to your Electron application.' will be displayed

@xfail
Scenario: Click button to start named greeting
    Given I have started the app
    When I click on the button 'Click me'
    Then the text 'Hello Maaeli' will be displayed