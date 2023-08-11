*** Settings ***
Resource    ../resources/variables.resource
Library     OperatingSystem
Library     String
Library     RequestsLibrary


*** Test Cases ***
Get First Author's Name
    [Documentation]    Retrieve the `name` of the first Author in the list.

Post Portrait
    [Documentation]    Upload the rf_logo.png from the /excercises folder as the
    ...                the portrait for one of the authors.
