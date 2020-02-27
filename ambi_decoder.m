function matrix = ambicodecmtrx(order, devices, mode)

%ambicodecmtrx computes encoder and decoder matrix for Higher Order

% Ambisonics (HOA)

%

% inputs

% order : Ambisonic order, integer value 0 through 7

% devices : array of azimuth, elevation and optional devicetype

% [azimuth; elevation; deviceType]

% [azimuth; elevation]

% where

% azimuth may range from 0 degrees to 360 degrees

% elevation may range from -90 degrees to 90 degrees

% deviceTypes are 0 or 1,

% deviceType turns the devices on or off for the

% particualar device. If deviceType vector is omitted,

% then the deviceTypes are set to 1.

% mode : 'enc' for encode matrix, 'dec' for decode matrx.

%

% outputs

% matrix : encode matrix of size [numDevices x numAmbisonicChannels] or

% decode matrix of size [numAmbisonicChannels x numDevices]

%

% This function ambicodecmtrx is for demonstration purposees. It is used in

% support of ambiencodemtrx and ambidecodemtrx. It may change in a future release.

% Copyright 2018 The Mathworks, Inc.

%#codegen

% -------------------------------------------------------------------------

% Validate required inputs

% -------------------------------------------------------------------------

validateattributes(order, {'numeric'}, ...

{'integer', '>=',0, '<=', 7, },...

'ambicodecmtrx', 'order', 1);

validateattributes(devices, {'single', 'double'}, ...

{'nonempty','2d','real','nonnan','finite'}, ...

'ambicodecmtrx', 'devices', 2);

mode = char(mode); % string support

% -------------------------------------------------------------------------

% Validate input data

% -------------------------------------------------------------------------

validateattributes(devices(1,:), {'single', 'double'}, ...

{'nonempty','>=',-360,'<=',360,'real','nonnan','finite'}, ...)

'ambicodecmtrx','azimuth')

azimuth = deg2rad(mod(devices(1, :), 360));

validateattributes(devices(2,:), {'single', 'double'}, ...

{'nonempty','>=',-90,'<=',90,'real','nonnan','finite'}, ...)

'ambicodecmtrx','elevation')

elevation = deg2rad(devices(2, :));

if size(devices, 1) == 2

deviceType = ones(1, size(devices, 2));

elseif size(devices, 1) == 3

validateattributes(devices(3, :), {'single', 'double'}, ...

{'nonempty','integer','>=',0,'<=',1,'real','nonnan','finite'}, ...) % REDUCED TO 0(OFF) and 1(ON)

'ambicodecmtrx','deviceType')

deviceType = devices(3, :);

end

% -------------------------------------------------------------------------

[~, numDevices] = size(devices);

if isa(devices,'single') || isa(order,'single')

matrixLegendre = zeros(numDevices, order2chan(order),'single');

else

matrixLegendre = zeros(numDevices, order2chan(order));

end

% ---------------------------------------------------------------------

c_az = cos(azimuth);

c_2az = cos(2*azimuth);

c_3az = cos(3*azimuth);

c_4az = cos(4*azimuth);

c_5az = cos(5*azimuth);

c_6az = cos(6*azimuth);

c_7az = cos(7*azimuth);

s_az = sin(azimuth);

s_2az = sin(2*azimuth);

s_3az = sin(3*azimuth);

s_4az = sin(4*azimuth);

s_5az = sin(5*azimuth);

s_6az = sin(6*azimuth);

s_7az = sin(7*azimuth);

c_el = cos(elevation);

c_el2 = c_el.*c_el;

c_el3 = c_el.*c_el.*c_el;

c_el4 = c_el.*c_el.*c_el.*c_el;

c_el5 = c_el.*c_el.*c_el.*c_el.*c_el;

c_el6 = c_el.*c_el.*c_el.*c_el.*c_el.*c_el;

c_el7 = c_el.*c_el.*c_el.*c_el.*c_el.*c_el.*c_el;

s_el = sin(elevation);

s_el2 = s_el.*s_el;

s_el3 = s_el.*s_el.*s_el;

s_el4 = s_el.*s_el.*s_el.*s_el;

s_el5 = s_el.*s_el.*s_el.*s_el.*s_el;

s_el6 = s_el.*s_el.*s_el.*s_el.*s_el.*s_el;

s_el7 = s_el.*s_el.*s_el.*s_el.*s_el.*s_el.*s_el;

s_2el = sin(2*elevation);

sqrt3 = sqrt(3);

sqrt5 = sqrt(5);

sqrt7 = sqrt(7);

sqrt15 = sqrt(15);

sqrt21 = sqrt(21);

sqrt35 = sqrt(35);

sqrt105 = sqrt(105);

sqrt231 = sqrt(231);

sqrt429 = sqrt(429);

sqrt3over2 = sqrt(3/2);

sqrt5over2 = sqrt(5/2);

sqrt7over2 = sqrt(7/2);

sqrt21over2 = sqrt(21/2);

sqrt35over2 = sqrt(35/2);

sqrt77over2 = sqrt(77/2);

sqrt105over2 = sqrt(105/2);

sqrt231over2 = sqrt(231/2);

sqrt1001over6 = sqrt(1001/6);

oneHalf = 1/2;

oneQuarter = 1/4;

oneEighth = 1/8;

threeEighth = 3/8;

oneSixteenth = 1/16;

threeSixteenths = 3/16;

oneThirtysecond = 1/32;

% ---------------------------------------------------------------------

% Zeroth Order

if order >= 0

matrixLegendre(:, 1) = 1; % W

end

% First Order

if order >= 1

matrixLegendre(:, 2) = s_az.*c_el; % Y

matrixLegendre(:, 3) = s_el; % Z

matrixLegendre(:, 4) = c_az.*c_el; % X

end

% Second Order

if order >= 2

matrixLegendre(:, 5)= oneHalf*sqrt3.*s_2az.*c_el2; % V

matrixLegendre(:, 6)= oneHalf*sqrt3.*s_az.*s_2el; % T

matrixLegendre(:, 7)= oneHalf*(3.*s_el.^2-1.); % R

matrixLegendre(:, 8)= oneHalf*sqrt3.*c_az.*s_2el; % S

matrixLegendre(:, 9)= oneHalf*sqrt3.*c_2az.*c_el2; % U

end

% Third Order

if order >= 3

matrixLegendre(:, 10) = oneHalf*sqrt5over2*s_3az.*c_el3; % Q

matrixLegendre(:, 11) = oneHalf*sqrt15*s_2az.*s_el.*c_el2; % O

matrixLegendre(:, 12) = oneHalf*sqrt3over2*s_az.*(5*s_el2-1.).*c_el; % M

matrixLegendre(:, 13) = oneHalf*s_el.*(5*s_el2-3.); % K

matrixLegendre(:, 14) = oneHalf*sqrt3over2*c_az.*(5*s_el2-1.).*c_el; % L

matrixLegendre(:, 15) = oneHalf*sqrt15*c_2az.*s_el.*c_el2; % N

matrixLegendre(:, 16) = oneHalf*sqrt5over2*c_3az.*c_el3; % P

end

% Fourth Order

if order >= 4

matrixLegendre(:, 17) = oneEighth*sqrt35*s_4az.*c_el4; % J

matrixLegendre(:, 18) = oneHalf*sqrt35over2*s_3az.*s_el.*c_el3; % H

matrixLegendre(:, 19) = oneQuarter*sqrt5*s_2az.*(7.*s_el2-1.).*c_el2; % F

matrixLegendre(:, 20) = oneHalf*sqrt5over2*s_az.*(7*s_el3-3*s_el).*c_el; % D

matrixLegendre(:, 21) = oneEighth*(35*s_el4-30*s_el2+3.); % B

matrixLegendre(:, 22) = oneHalf*sqrt5over2*c_az.*(7*s_el3-3*s_el).*c_el; % C

matrixLegendre(:, 23) = oneQuarter*sqrt5*c_2az.*(7*s_el2-1).*c_el2; % E

matrixLegendre(:, 24) = oneHalf*sqrt35over2*c_3az.*s_el.*c_el3; % G

matrixLegendre(:, 25) = oneEighth*sqrt35*c_4az.*c_el4; % I

end

% Fifth Order

if order >= 5

matrixLegendre(:, 26) = threeEighth*sqrt7over2*s_5az.*c_el5;

matrixLegendre(:, 27) = threeEighth*sqrt35*s_4az.*s_el.*c_el4;

matrixLegendre(:, 28) = oneEighth*sqrt35over2*s_3az.*(9*s_el2-1).*c_el3;

matrixLegendre(:, 29) = oneQuarter*sqrt105*s_2az.*(3*s_el3-s_el).*c_el2;

matrixLegendre(:, 30) = oneEighth*sqrt15*s_az.*(21*s_el4-14*s_el2+1).*c_el;

matrixLegendre(:, 31) = oneEighth*(63*s_el5-70*s_el3+15*s_el);

matrixLegendre(:, 32) = oneEighth*sqrt15*c_az.*(21*s_el4-14*s_el2+1).*c_el;

matrixLegendre(:, 33) = oneQuarter*sqrt105*c_2az.*(3*s_el3-s_el).*c_el2;

matrixLegendre(:, 34) = oneEighth*sqrt35over2*c_3az.*(9*s_el2-1).*c_el3;

matrixLegendre(:, 35) = threeEighth*sqrt35*c_4az.*s_el.*c_el4;

matrixLegendre(:, 36) = threeEighth*sqrt7over2*c_5az.*c_el5;

end

% Sixth Order

if order >= 6

matrixLegendre(:, 37) = oneSixteenth*sqrt231over2*s_6az.*c_el6;

matrixLegendre(:, 38) = threeEighth*sqrt77over2*s_5az.*s_el.*c_el5;

matrixLegendre(:, 39) = threeSixteenths*sqrt7*s_4az.*(11*s_el2-1).*c_el4;

matrixLegendre(:, 40) = oneEighth*sqrt105over2*s_3az.*(11*s_el3-3*s_el).*c_el3;

matrixLegendre(:, 41) = oneSixteenth*sqrt105over2*s_2az.*(33*s_el4-18*s_el2+1).*c_el2;

matrixLegendre(:, 42) = oneEighth*sqrt21*s_az.*(33*s_el5-30*s_el3+5*s_el).*c_el;

matrixLegendre(:, 43) = oneSixteenth*(231*s_el6-315*s_el4+105*s_el2-5);

matrixLegendre(:, 44) = oneEighth*sqrt21*c_az.*(33*s_el5-30*s_el3+5*s_el).*c_el;

matrixLegendre(:, 45) = oneSixteenth*sqrt105over2*c_2az.*(33*s_el4-18*s_el2+1).*c_el2;

matrixLegendre(:, 46) = oneEighth*sqrt105over2*c_3az.*(11*s_el3-3*s_el).*c_el3;

matrixLegendre(:, 47) = threeSixteenths*sqrt7*c_4az.*(11*s_el2-1).*c_el4;

matrixLegendre(:, 48) = threeEighth*sqrt77over2*c_5az.*s_el.*c_el5;

matrixLegendre(:, 49) = oneSixteenth*sqrt231over2*c_6az.*c_el6;

end

% seventh order

if order >= 7

matrixLegendre(:, 50) = oneThirtysecond*sqrt429*s_7az.*c_el7;

matrixLegendre(:, 51) = threeSixteenths*sqrt1001over6*s_6az.*s_el.*c_el6;

matrixLegendre(:, 52) = oneThirtysecond*sqrt231*s_5az.*(13*s_el2-1).*c_el5;

matrixLegendre(:, 53) = oneSixteenth*sqrt231*s_4az.*(13*s_el3-3*s_el).*c_el4;

matrixLegendre(:, 54) = oneThirtysecond*sqrt21*s_3az.*(143*s_el4-66*s_el2+3).*c_el3;

matrixLegendre(:, 55) = oneSixteenth*sqrt21over2*s_2az.*(143*s_el5-110*s_el3+15*s_el).*c_el2;

matrixLegendre(:, 56) = oneThirtysecond*sqrt7*s_az.*(429*s_el6-495*s_el4+135*s_el2-5).*c_el;

matrixLegendre(:, 57) = oneSixteenth*(429*s_el7-693*s_el5+315*s_el3-35*s_el);

matrixLegendre(:, 58) = oneThirtysecond*sqrt7*c_az.*(429*s_el6-495*s_el4+135*s_el2-5).*c_el;

matrixLegendre(:, 59) = oneSixteenth*sqrt21over2*c_2az.*(143*s_el5-110*s_el3+15*s_el).*c_el2;

matrixLegendre(:, 60) = oneThirtysecond*sqrt21*c_3az.*(143*s_el4-66*s_el2+3).*c_el3;

matrixLegendre(:, 61) = oneSixteenth*sqrt231*c_4az.*(13*s_el3-3*s_el).*c_el4;

matrixLegendre(:, 62) = oneThirtysecond*sqrt231*c_5az.*(13*s_el2-1).*c_el5;

matrixLegendre(:, 63) = threeSixteenths*sqrt1001over6*c_6az.*s_el.*c_el6;

matrixLegendre(:, 64) = oneThirtysecond*sqrt429*c_7az.*c_el7;

end

% -------------------------------------------------------------------------

matrixLegendre((deviceType == 0),:) = 0; % apply deviceType 0(OFF) mask

switch mode

case 'enc'

matrix = matrixLegendre;

case 'dec'

matrix = pinv(matrixLegendre);

otherwise

coder.internal.error('audio:ambisonics:modeInvalid', mode);

end

% -------------------------------------------------------------------------

function channels = order2chan(order)

channels = (order+1)^2;

end

end