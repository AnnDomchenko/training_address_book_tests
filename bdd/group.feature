Feature: Group feature
  Description

  Scenario Outline: Add new group
    Given a group list
    Given a group with <name>, <header>, <footer>
    When I add this new group to the list
    Then a new group list is equal to the old list with the new group

    Examples:
    | name   | header | footer   |
    | as dfg | gf     | fdgdh    |
    | 13214  |  12    | ?*)"'    |
    |  рпмрп | аыавыа |  ыавыаы  |

  Scenario: Delete a random group
    Given a non-empty group list
    Given a random group
    When I delete the group
    Then the new group list is equal to the old list without the deleted group
