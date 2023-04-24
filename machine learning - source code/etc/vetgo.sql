drop database if exists vetgo;
create database if not exists vetgo;
use vetgo;

create table if not exists petOwner (
	petOwner_id int unsigned not null auto_increment primary key,
    firstname varchar(30) not null,
    lastname varchar(30) not null,
    middleInit varchar(1),
    pw varchar(255) not null,
    email varchar(255) unique not null,		## used also for logging in
    #foreign key(address_id) references address(address_id) on delete cascade,
    #foreign key(pet_id) references pet(pet_id) on delete cascade,
    check (pw like '%[0-9]%' and pw like '%[A-Z]%' and pw like '%[!@#$%^&*()]%' and length(pw) >= 8 and length(pw) <= 20),
    check (middleInit like '%[A-Z]%'and length(pw) = 1)
);

create table if not exists clinic (
	clinic_id int unsigned not null auto_increment primary key,
	streetAddr1 varchar(255) not null,
    streetAddr2 varchar(20),
    city varchar(50) not null,
    stateAbbr varchar(2) not null,
	country varchar(15) not null,
    zipcode int unsigned not null
);

create table if not exists veterinarian (
	vet_registered_number int unsigned not null primary key,
    firstname varchar(30) not null,
    lastname varchar(30) not null,
    middleInit varchar(1),
    pw varchar(255) not null,
    email varchar(255) unique not null,
    clinic int unsigned not null,
    foreign key(clinic) references clinic(clinic_id),
    check (pw like '%[0-9]%' and pw like '%[A-Z]%' and pw like '%[!@#$%^&*()]%' and length(pw) >= 8 and length(pw) <= 20),
    check (middleInit like '%[A-Z]%'and length(pw) = 1)
);

create table if not exists pet (
	pet_id int unsigned not null auto_increment primary key,
    guardian int unsigned,
    vet int unsigned,
    foreign key(guardian) references petOwner(petOwner_id),
    foreign key(vet) references veterinarian(vet_registered_number)
);

create table if not exists dog (
	pet_id int unsigned not null primary key references pet(pet_id),
    breed varchar(255),
    color varchar(20),
    physicalDesc varchar(255),
    age int unsigned,
    dob varchar(10),
    reproStatus varchar(15),
    foreign key(pet_id) references pet(pet_id),
    microchip_id int unsigned
);

create table if not exists cat (
	pet_id int unsigned not null primary key references pet(pet_id),
    breed varchar(255),
    color varchar(20),
    physicalDesc varchar(255),
    age int unsigned,
    dob varchar(10),
    reproStatus varchar(15),
    foreign key(pet_id) references pet(pet_id),
    microchip_id int unsigned
);

create table if not exists paymentInfo (
    cardNum int unsigned not null primary key,
	expDate varchar(4) not null,
    cvv int unsigned not null,
    cardholderFirstname varchar(255) not null,
    cardholderLastname varchar(255) not null,
    ##foreign key(billingAddr) references address(address_id),
    registeredTo int unsigned not null,
    foreign key(registeredTo) references petOwner(petOwner_id)
);

create table if not exists address (
	address_id int unsigned not null auto_increment primary key,
	streetAddr1 varchar(255) not null,
    streetAddr2 varchar(20),
    city varchar(50) not null,
    stateAbbr varchar(2) not null,
	country varchar(15) not null,
    zipcode int unsigned not null,
    physicalAddrOf int unsigned not null,
    billingAddrOf int unsigned not null,
    foreign key(physicalAddrOf) references petOwner(petOwner_id) on delete cascade,
    foreign key(billingAddrOf) references paymentInfo(cardNum) on delete cascade
);

create table if not exists symptom (
	symptom_id int unsigned not null auto_increment primary key,
    symptomDescription varchar(255) not null,
    symptopmName varchar(255) not null
);

create table if not exists record (
	record_id int unsigned not null auto_increment primary key,
    vacHistory varchar(255),
    pastTreatment varchar(255),
    currTreatment varchar(255),
    pastMed varchar(255),
    currMed varchar(255),
    testRecord varchar(255),
    surgRecord varchar(255),
    weightHistory varchar(255),
    pet_id int unsigned not null,
    symptom_id int unsigned,
    foreign key(pet_id) references pet(pet_id),
    foreign key(symptom_id) references symptom(symptom_id)
);