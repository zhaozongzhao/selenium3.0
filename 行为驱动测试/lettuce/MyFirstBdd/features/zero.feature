Feature:Compute factorial
  In order to place with Lettuce
  As beginners
  we'll implement factorial

  Scenario: Factorial of 0
    Given I have the number 0
    When I  compute its factorial
    Then I See the number 1