[Timestamp]: (./Timestamp.md)

# Logical description of pages

This page lists the logical description and use of Calico Pages.

## Data

A page is constructed to be very versatile, not necessarily efficient.

> This structure uses another structure, [Timestamp](Timestamp).

### Logical Structure

<table style="text-align: center;">
    <tr>
        <th colspan=5> Page Title </th>
        <th colspan=1> Project </th>
    </tr> <tr>
        <td colspan=2> Page ID </td>
        <td colspan=2> Parent ID </td>
        <td colspan=2> Workspace ID </td>
    </tr> <tr>
        <td colspan=2> Event times </td>
        <td colspan=2> Tracked times </td>
        <td colspan=2> Due </td>
    </tr> <tr>
        <td colspan=1> Completion </td>
        <td colspan=1> Priority </td>
        <td colspan=2> Tags </td>
        <td colspan=2> Assignees </td>
    </tr>
</table>

### Logical definitions

Name          | Logical encoding         | Data Type
--------------|--------------------------|----------
Page Title    | None                     | `String`
Project       | None                     | `bool`
||
Page ID       | None                     | `int`
Parent ID     | None                     | `int`
||
Event times   | [Timestamp](Timestamp)   | `[Timestamp]`
Tracked time  | [Timestamp](Timestamp)   | `[Timestamp]`
Due           | [Timestamp](Timestamp)   | `Timestamp`
||
Completion    | None                     | `bool`
Priority      | None                     | `int`
Tags          | None                     | `[str]`
Assignees     | None                     | `[int]`

### Table Structure

| Page Title | Project | Page ID | Parent ID | Workspace ID | Event Times | Tracked Times | Due | Completion | Priority | Tags | Assignees |
|-|-|-|-|-|-|-|-|-|-|-|-|
| Calico | True | 00000004 | 00000003 | 00000001 | None | None | None | False | 1 | ["Documentation"] | [00000001] |
| Finish projects description | False | 00000004 | 00000003 | 00000001 | [{ "start": 1541584800, "duration": 3600, "offset": None, }] | None | { "start": 1542672000, "duration": None, "offset": None, } | False | 1 | ["Documentation"] | [00000001] |

