# new-horizons
Simple Text UI based program for tracking Animal Crossing: New Horizons inventory

## Motivation
Reduce the time needed to determine what item should be dropped from character inventory to maximize sale price of inventory

## Demonstrates
- Data Structures & Algorithms
- Python
- Text UI application

## Installation

1. git clone http://github.com/tyfoster97/new-horizons.git

## Use

1. Navigate to directory containing main.py
2. From command line type 'python3 main.py'
3. Execute commands below until done

## Commands

**ai {name}**:
> add insect with {name} to inventory

**af {name}**:
> add fish with {name} to inventory

**am {name}**:
> add miscilaneous object with {name} to inventory

**ci {name}**:
> compare insect with {name} against inventory
> returns names and prices of items less than insect price

**cf {name}**:
> compare fish with {name} against inventory
> returns names and prices of items less than fish price

**cm {name}**:
> compare miscelaneous item with {name} against inventory
> returns names and prices of items less than item price

**l**:
> list inventory items

**q**:
> quit

**r {name}**:
> remove item with {name} from inventory

**si {name}**:
> return information about insect with {name}

**sf {name}**:
> return information about fish with {name}

**sm {name}**:
> return information about miscelaneous item with {name}

**su-in**:
> edit insect database

**su-fi**:
> edit fish database

**su-mi**:
> edit misc database

**w**:
> sell items in inventory
