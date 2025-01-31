# ------------------------------------------------------------------------------
# <auto-generated>
#     This code was generated by a tool.
#     Changes to this file may cause incorrect behavior and will be lost if
#     the code is regenerated.
# </auto-generated>
#
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# ------------------------------------------------------------------------------

from .base_date_time import BaseDateTime
# pylint: disable=line-too-long


class SpanishDateTime:
    TillRegex = f'(?<till>hasta|al|a|--|-|—|——)(\\s+(el|la(s)?))?'
    AndRegex = f'(?<and>y|y\\s*el|--|-|—|——)'
    DayRegex = f'(?<day>01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|1|20|21|22|23|24|25|26|27|28|29|2|30|31|3|4|5|6|7|8|9)(?=\\b|t)'
    MonthNumRegex = f'(?<month>01|02|03|04|05|06|07|08|09|10|11|12|1|2|3|4|5|6|7|8|9)\\b'
    AmDescRegex = f'({BaseDateTime.BaseAmDescRegex})'
    PmDescRegex = f'({BaseDateTime.BasePmDescRegex})'
    AmPmDescRegex = f'({BaseDateTime.BaseAmPmDescRegex})'
    DescRegex = f'(?<desc>({AmDescRegex}|{PmDescRegex}))'
    OfPrepositionRegex = f'(do|da|del|de)'
    AfterNextSuffixRegex = f'\\b(que\\s+viene|pasad[oa])\\b'
    RangePrefixRegex = f'((desde|de|entre)\\s+(la(s)?\\s+)?)'
    TwoDigitYearRegex = f'\\b(?<![$])(?<year>([0-27-9]\\d))(?!(\\s*((\\:)|{AmDescRegex}|{PmDescRegex}|\\.\\d)))\\b'
    RelativeRegex = f'(?<rela>((esta|este|pr[oó]xim[oa]|([uú]ltim(o|as|os)))(\\s+fin(ales)?\\s+de(\\s+la)?)?)|(fin(ales)?\\s+de(\\s+la)?))\\b'
    StrictRelativeRegex = f'(?<rela>((esta|este|pr[oó]xim[oa]|([uú]ltim(o|as|os)))(\\s+fin(ales)?\\s+de(\\s+la)?)?)|(fin(ales)?\\s+de(\\s+la)?))\\b'
    WrittenOneToNineRegex = f'(uno|un|una|dos|tres|cuatro|cinco|seis|siete|ocho|nueve)'
    WrittenOneHundredToNineHundredRegex = f'(cien|ciento|doscient[oa]s|trescient[oa]s|cuatrocient[ao]s|quinient[ao]s|seiscient[ao]s|setecient[ao]s|ochocient[ao]s|novecient[ao]s)'
    WrittenOneToNinetyNineRegex = f'(uno|un|una|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|catorce|quince|dieciséis|dieciseis|diecisiete|dieciocho|diecinueve|veinte|veintiuno|veintiún|veintiun|veintiuna|veintidós|veintidos|veintitrés|veintitres|veinticuatro|veinticinco|veintiséis|veintisiete|veintiocho|veintinueve|((treinta|cuarenta|cincuenta|sesenta|setenta|ochenta|noventa)(\\s+y\\s+{WrittenOneToNineRegex})?))'
    FullTextYearRegex = f'(((dos\\s+)?mil)(\\s+{WrittenOneHundredToNineHundredRegex})?(\\s+{WrittenOneToNinetyNineRegex})?)'
    YearRegex = f'({BaseDateTime.FourDigitYearRegex}|{FullTextYearRegex})'
    RelativeMonthRegex = f'(?<relmonth>((este|pr[oó]ximo|([uú]ltim(o|as|os)))\\s+mes)|(mes\\s+((que\\s+viene)|pasado)))\\b'
    MonthRegex = f'\\b(?<month>abril|abr|agosto|ago|diciembre|dic|febrero|feb|enero|ene|julio|jul|junio|jun|marzo|mar|mayo|may|noviembre|nov|octubre|oct|septiembre|setiembre|sept|set|sep)\\b'
    MonthSuffixRegex = f'(?<msuf>((del|de|la|el)\\s+)?({RelativeMonthRegex}|{MonthRegex}))'
    DateUnitRegex = f'(?<unit>años?|mes(es)?|semanas?|d[ií]as?)\\b'
    PastRegex = f'(?<past>\\b(pasad(a|o)(s)?|[uú]ltim[oa](s)?|anterior(es)?|previo(s)?)\\b)'
    FutureRegex = f'(?<past>\\b(siguiente(s)?|pr[oó]xim[oa](s)?|dentro\\s+de|en)\\b)'
    SimpleCasesRegex = f'\\b((desde\\s+el|desde|del|de)\\s+)?({DayRegex})\\s*{TillRegex}\\s*({DayRegex})\\s+{MonthSuffixRegex}((\\s+|\\s*,\\s*)(en\\s+|del\\s+|de\\s+)?{YearRegex})?\\b'
    MonthFrontSimpleCasesRegex = f'\\b{MonthSuffixRegex}\\s+((desde\\s+el|desde|del)\\s+)?({DayRegex})\\s*{TillRegex}\\s*({DayRegex})((\\s+|\\s*,\\s*)(en\\s+|del\\s+|de\\s+)?{YearRegex})?\\b'
    MonthFrontBetweenRegex = f'\\b{MonthSuffixRegex}\\s+((entre|entre\\s+el)\\s+)({DayRegex})\\s*{AndRegex}\\s*({DayRegex})((\\s+|\\s*,\\s*)(en\\s+|del\\s+|de\\s+)?{YearRegex})?\\b'
    DayBetweenRegex = f'\\b((entre|entre\\s+el)\\s+)({DayRegex})(\\s+{MonthSuffixRegex})?\\s*{AndRegex}\\s*({DayRegex})\\s+{MonthSuffixRegex}((\\s+|\\s*,\\s*)(en\\s+|del\\s+|de\\s+)?{YearRegex})?\\b'
    OneWordPeriodRegex = f'\\b(((((la|el)\\s+)?mes\\s+(({OfPrepositionRegex})\\s+))|((pr[oó]xim[oa]?|est[ea]|[uú]ltim[oa]?)\\s+))?({MonthRegex})|((la|el)\\s+)?((({RelativeRegex}\\s+){DateUnitRegex}(\\s+{AfterNextSuffixRegex})?)|{DateUnitRegex}(\\s+{AfterNextSuffixRegex}))|va\\s+de\\s+{DateUnitRegex})'
    MonthWithYearRegex = f'\\b(((pr[oó]xim[oa](s)?|este|esta|[uú]ltim[oa]?)\\s+)?({MonthRegex})(\\s+|(\\s*[,-]\\s*))((de|del|de la)\\s+)?({YearRegex}|(?<order>pr[oó]ximo(s)?|[uú]ltimo?|este)\\s+año))\\b'
    MonthNumWithYearRegex = f'({YearRegex}(\\s*?)[/\\-\\.~](\\s*?){MonthNumRegex})|({MonthNumRegex}(\\s*?)[/\\-\\.~](\\s*?){YearRegex})'
    WeekOfMonthRegex = f'(?<wom>(la\\s+)?(?<cardinal>primera?|1ra|segunda|2da|tercera?|3ra|cuarta|4ta|quinta|5ta|[uú]ltima)\\s+semana\\s+{MonthSuffixRegex})'
    WeekOfYearRegex = f'(?<woy>(la\\s+)?(?<cardinal>primera?|1ra|segunda|2da|tercera?|3ra|cuarta|4ta|quinta|5ta|[uú]ltima?|([12345]ª))\\s+semana(\\s+del?)?\\s+({YearRegex}|(?<order>pr[oó]ximo|[uú]ltimo|este)\\s+año))'
    FollowedDateUnit = f'^\\s*{DateUnitRegex}'
    NumberCombinedWithDateUnit = f'\\b(?<num>\\d+(\\.\\d*)?){DateUnitRegex}'
    QuarterTermRegex = f'(?<cardinal>primer|1er|segundo|2do|tercer|3ro|4to|((1|2|3|4)º))\\s+(cuatrimestre|cuarto)'
    QuarterRegex = f'(el\\s+)?{QuarterTermRegex}((\\s+del?|\\s*,\\s*)?\\s+({YearRegex}|(?<order>pr[oó]ximo(s)?|[uú]ltimo?|este)\\s+a[ñn]o|a[ñn]o(\\s+{AfterNextSuffixRegex})))?'
    QuarterRegexYearFront = f'({YearRegex}|(?<order>pr[oó]ximo(s)?|[uú]ltimo?|este)\\s+a[ñn]o)\\s+(el\\s+)?{QuarterTermRegex}'
    AllHalfYearRegex = f'^[.]'
    EarlyPrefixRegex = f'\\b(?<EarlyPrefix>((comienzos|inicios)\\s+({OfPrepositionRegex})))\\b'
    MidPrefixRegex = f'\\b(?<MidPrefix>(mediados\\s+({OfPrepositionRegex})))\\b'
    LaterPrefixRegex = f'\\b(?<LatePrefix>((fines|finales)\\s+({OfPrepositionRegex})))\\b'
    PrefixPeriodRegex = f'({EarlyPrefixRegex}|{MidPrefixRegex}|{LaterPrefixRegex})'
    PrefixDayRegex = f'^[.]'
    CenturySuffixRegex = f'^[.]'
    SeasonRegex = f'\\b(?<season>(([uú]ltim[oa]|est[ea]|el|la|(pr[oó]xim[oa]s?|siguiente)|{PrefixPeriodRegex})\\s+)?(?<seas>primavera|verano|otoño|invierno)((\\s+del?|\\s*,\\s*)?\\s+({YearRegex}|(?<order>pr[oó]ximo|[uú]ltimo|este)\\s+año))?)\\b'
    WhichWeekRegex = f'\\b(semana)(\\s*)(?<number>5[0-3]|[1-4]\\d|0?[1-9])\\b'
    WeekOfRegex = f'((del|de|la|el)\\s+)?(semana)(\\s*)({OfPrepositionRegex})'
    MonthOfRegex = f'(mes)(\\s+)({OfPrepositionRegex})'
    RangeUnitRegex = f'\\b(?<unit>años|año|meses|mes|semanas|semana)\\b'
    InConnectorRegex = f'\\b(in)\\b'
    SinceYearSuffixRegex = f'^[.]'
    WithinNextPrefixRegex = f'\\b(dentro\\s+de)\\b'
    FromRegex = f'((desde|de)(\\s*la(s)?)?)$'
    ConnectorAndRegex = f'(y\\s*(la(s)?)?)$'
    BetweenRegex = f'(entre\\s*(la(s)?)?)'
    WeekDayRegex = f'\\b(?<weekday>domingos?|lunes|martes|mi[eé]rcoles|jueves|viernes|s[aá]bados?|lun|mar|mi[eé]|jue|vie|s[aá]b|dom|lu|ma|mi|ju|vi|sa|do)\\b'
    OnRegex = f'(?<=\\ben\\s+)({DayRegex}s?)\\b'
    RelaxedOnRegex = f'(?<=\\b(en|el|del)\\s+)((?<day>10|11|12|13|14|15|16|17|18|19|1st|20|21|22|23|24|25|26|27|28|29|2|30|31|3|4|5|6|7|8|9)s?)\\b'
    ThisRegex = f'\\b((este\\s*){WeekDayRegex})|({WeekDayRegex}\\s*((de\\s+)?esta\\s+semana))\\b'
    LastDateRegex = f'\\b(([uú]ltimo)\\s*{WeekDayRegex})|({WeekDayRegex}(\\s+((de\\s+)?(esta|la)\\s+([uú]ltima\\s+)?semana)))\\b'
    NextDateRegex = f'\\b(((pr[oó]ximo|siguiente)\\s*){WeekDayRegex})|({WeekDayRegex}(\\s+(de\\s+)?(la\\s+)?(pr[oó]xima|siguiente)(\\s*semana)))\\b'
    SpecialDayRegex = f'\\b((el\\s+)?(d[ií]a\\s+antes\\s+de\\s+ayer|anteayer)|((el\\s+)?d[ií]a\\s+(despu[eé]s\\s+)?de\\s+mañana|pasado\\s+mañana)|(el\\s)?d[ií]a siguiente|(el\\s)?pr[oó]ximo\\s+d[ií]a|(el\\s+)?[uú]ltimo d[ií]a|(d)?el d[ií]a|ayer|mañana|hoy)\\b'
    SpecialDayWithNumRegex = f'^[.]'
    ForTheRegex = f'^[.]'
    WeekDayAndDayOfMonthRegex = f'^[.]'
    WeekDayAndDayRegex = f'^[.]'
    WeekDayOfMonthRegex = f'(?<wom>(el\\s+)?(?<cardinal>primer|1er|segundo|2do|tercer|3er|cuarto|4to|quinto|5to|[uú]ltimo)\\s+{WeekDayRegex}\\s+{MonthSuffixRegex})'
    RelativeWeekDayRegex = f'^[.]'
    NumberEndingPattern = f'^[.]'
    SpecialDateRegex = f'(?<=\\b(en)\\s+el\\s+){DayRegex}\\b'
    OfMonthRegex = f'^\\s*de\\s*{MonthSuffixRegex}'
    MonthEndRegex = f'({MonthRegex}\\s*(el)?\\s*$)'
    WeekDayEnd = f'{WeekDayRegex}\\s*,?\\s*$'
    WeekDayStart = f'^[\\.]'
    DateYearRegex = f'(?<year>{YearRegex}|{TwoDigitYearRegex})'
    DateExtractor1 = f'\\b({WeekDayRegex}(\\s+|\\s*,\\s*))?{DayRegex}?((\\s*(de)|[/\\\\\\.\\-])\\s*)?{MonthRegex}\\b'
    DateExtractor2 = f'\\b({WeekDayRegex}(\\s+|\\s*,\\s*))?{DayRegex}\\s*([\\.\\-]|de)\\s*{MonthRegex}(\\s*,\\s*|\\s*(del?)\\s*){DateYearRegex}\\b'
    DateExtractor3 = f'\\b({WeekDayRegex}(\\s+|\\s*,\\s*))?{DayRegex}(\\s+|\\s*,\\s*|\\s+de\\s+|\\s*-\\s*){MonthRegex}((\\s+|\\s*,\\s*){DateYearRegex})?\\b'
    DateExtractor4 = f'\\b{MonthNumRegex}\\s*[/\\\\\\-]\\s*{DayRegex}\\s*[/\\\\\\-]\\s*{DateYearRegex}'
    DateExtractor5 = f'\\b{DayRegex}\\s*[/\\\\\\-\\.]\\s*({MonthNumRegex}|{MonthRegex})\\s*[/\\\\\\-\\.]\\s*{DateYearRegex}'
    DateExtractor6 = f'(?<=\\b(en|el)\\s+){MonthNumRegex}[\\-\\.]{DayRegex}\\b'
    DateExtractor7 = f'\\b{MonthNumRegex}\\s*/\\s*{DayRegex}((\\s+|\\s*,\\s*|\\s+de\\s+){DateYearRegex})?\\b'
    DateExtractor8 = f'(?<=\\b(en|el)\\s+){DayRegex}[\\\\\\-]{MonthNumRegex}\\b'
    DateExtractor9 = f'\\b{DayRegex}\\s*/\\s*{MonthNumRegex}((\\s+|\\s*,\\s*|\\s+de\\s+){DateYearRegex})?\\b'
    DateExtractor10 = f'\\b{YearRegex}\\s*[/\\\\\\-\\.]\\s*{MonthNumRegex}\\s*[/\\\\\\-\\.]\\s*{DayRegex}'
    HourNumRegex = f'\\b(?<hournum>cero|una|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce)\\b'
    MinuteNumRegex = f'(?<minnum>un|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|catorce|quince|dieciseis|diecisiete|dieciocho|diecinueve|veinte|treinta|cuarenta|cincuenta)'
    DeltaMinuteNumRegex = f'(?<deltaminnum>un|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|catorce|quince|dieciseis|diecisiete|dieciocho|diecinueve|veinte|treinta|cuarenta|cincuenta)'
    OclockRegex = f'(?<oclock>en\\s+punto)'
    PmRegex = f'(?<pm>((por|de|a|en)\\s+la)\\s+(tarde|noche))'
    AmRegex = f'(?<am>((por|de|a|en)\\s+la)\\s+(mañana|madrugada))'
    AmTimeRegex = f'(?<am>(esta|(por|de|a|en)\\s+la)\\s+(mañana|madrugada))'
    PmTimeRegex = f'(?<pm>(esta|(por|de|a|en)\\s+la)\\s+(tarde|noche))'
    LessThanOneHour = f'(?<lth>((\\s+y\\s+)?cuarto|(\\s*)menos cuarto|(\\s+y\\s+)media|{BaseDateTime.DeltaMinuteRegex}(\\s+(minuto|minutos|min|mins))|{DeltaMinuteNumRegex}(\\s+(minuto|minutos|min|mins))))'
    TensTimeRegex = f'(?<tens>diez|veint(i|e)|treinta|cuarenta|cincuenta)'
    WrittenTimeRegex = f'(?<writtentime>{HourNumRegex}\\s*((y|menos)\\s+)?({MinuteNumRegex}|({TensTimeRegex}((\\s*y\\s+)?{MinuteNumRegex})?)))'
    TimePrefix = f'(?<prefix>{LessThanOneHour}(\\s+(pasad[ao]s)\\s+(de\\s+las|las)?|\\s+(para|antes\\s+de)?\\s+(las?))?)'
    TimeSuffix = f'(?<suffix>({LessThanOneHour}\\s+)?({AmRegex}|{PmRegex}|{OclockRegex}))'
    BasicTime = f'(?<basictime>{WrittenTimeRegex}|{HourNumRegex}|{BaseDateTime.HourRegex}:{BaseDateTime.MinuteRegex}(:{BaseDateTime.SecondRegex})?|{BaseDateTime.HourRegex})'
    AtRegex = f'\\b(?<=\\b(a las?)\\s+)({WrittenTimeRegex}|{HourNumRegex}|{BaseDateTime.HourRegex})\\b(\\s*\\bh\\b)?'
    ConnectNumRegex = f'({BaseDateTime.HourRegex}(?<min>00|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|53|54|55|56|57|58|59)\\s*{DescRegex})'
    TimeRegex1 = f'(\\b{TimePrefix}\\s+)?({WrittenTimeRegex}|{HourNumRegex}|{BaseDateTime.HourRegex})\\s*({DescRegex}|\\s*\\bh\\b)'
    TimeRegex2 = f'(\\b{TimePrefix}\\s+)?(t)?{BaseDateTime.HourRegex}(\\s*)?:(\\s*)?{BaseDateTime.MinuteRegex}((\\s*)?:(\\s*)?{BaseDateTime.SecondRegex})?((\\s*{DescRegex})|\\b)'
    TimeRegex3 = f'(\\b{TimePrefix}\\s+)?{BaseDateTime.HourRegex}\\.{BaseDateTime.MinuteRegex}(\\s*({DescRegex}|\\bh\\b))'
    TimeRegex4 = f'\\b(({DescRegex}?)|({BasicTime}?)({DescRegex}?))({TimePrefix}\\s*)({HourNumRegex}|{BaseDateTime.HourRegex})?(\\s+{TensTimeRegex}(\\s+y\\s+)?{MinuteNumRegex}?)?({OclockRegex})?\\b'
    TimeRegex5 = f'\\b({TimePrefix}|{BasicTime}{TimePrefix})\\s+(\\s*{DescRegex})?{BasicTime}?\\s*{TimeSuffix}\\b'
    TimeRegex6 = f'({BasicTime}(\\s*{DescRegex})?\\s+{TimeSuffix}\\b)'
    TimeRegex7 = f'\\b{TimeSuffix}\\s+a\\s+las\\s+{BasicTime}((\\s*{DescRegex})|\\b)'
    TimeRegex8 = f'\\b{TimeSuffix}\\s+{BasicTime}((\\s*{DescRegex})|\\b)'
    TimeRegex9 = f'\\b(?<writtentime>{HourNumRegex}\\s+({TensTimeRegex}\\s*)?(y\\s+)?{MinuteNumRegex}?)\\b'
    TimeRegex10 = f'(a\\s+la|al)\\s+(madrugada|mañana|medio\\s*d[ií]a|tarde|noche)'
    TimeRegex11 = f'\\b({WrittenTimeRegex})({DescRegex}?)\\b'
    TimeRegex12 = f'(\\b{TimePrefix}\\s+)?{BaseDateTime.HourRegex}(\\s*h\\s*){BaseDateTime.MinuteRegex}(\\s*{DescRegex})?'
    PrepositionRegex = f'\\b(?<prep>(a(l)?|en|de(l)?)?(\\s*(la(s)?|el|los))?$)\\b'
    NowRegex = f'\\b(?<now>(justo\\s+)?ahora(\\s+mismo)?|en\\s+este\\s+momento|tan\\s+pronto\\s+como\\s+sea\\s+posible|tan\\s+pronto\\s+como\\s+(pueda|puedas|podamos|puedan)|lo\\s+m[aá]s\\s+pronto\\s+posible|recientemente|previamente)\\b'
    SuffixRegex = f'^\\s*(((y|a|en|por)\\s+la|al)\\s+)?(mañana|madrugada|medio\\s*d[ií]a|tarde|noche)\\b'
    TimeOfDayRegex = f'\\b(?<timeOfDay>mañana|madrugada|(pasado\\s+(el\\s+)?)?medio\\s?d[ií]a|tarde|noche|anoche)\\b'
    SpecificTimeOfDayRegex = f'\\b(((((a\\s+)?la|esta|siguiente|pr[oó]xim[oa]|[uú]ltim[oa])\\s+)?{TimeOfDayRegex}))\\b'
    TimeOfTodayAfterRegex = f'^\\s*(,\\s*)?(en|de(l)?\\s+)?{SpecificTimeOfDayRegex}'
    TimeOfTodayBeforeRegex = f'({SpecificTimeOfDayRegex}(\\s*,)?(\\s+(a\\s+la(s)?|para))?\\s*)'
    SimpleTimeOfTodayAfterRegex = f'({HourNumRegex}|{BaseDateTime.HourRegex})\\s*(,\\s*)?((en|de(l)?)?\\s+)?{SpecificTimeOfDayRegex}'
    SimpleTimeOfTodayBeforeRegex = f'({SpecificTimeOfDayRegex}(\\s*,)?(\\s+(a\\s+la|para))?\\s*({HourNumRegex}|{BaseDateTime.HourRegex}))'
    SpecificEndOfRegex = f'((a|e)l\\s+)?fin(alizar|al)?(\\s+(el|de(l)?)(\\s+d[ií]a)?(\\s+de)?)?\\s*$'
    UnspecificEndOfRegex = f'^[.]'
    UnspecificEndOfRangeRegex = f'^[.]'
    UnitRegex = f'(?<unit>años|año|meses|mes|semanas|semana|d[ií]as|d[ií]a|horas|hora|h|hr|hrs|hs|minutos|minuto|mins|min|segundos|segundo|segs|seg)\\b'
    ConnectorRegex = f'^(,|t|para la|para las|cerca de la|cerca de las)$'
    TimeHourNumRegex = f'(?<hour>veintiuno|veintidos|veintitres|veinticuatro|cero|uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|catorce|quince|diecis([eé])is|diecisiete|dieciocho|diecinueve|veinte)'
    PureNumFromTo = f'((desde|de)\\s+(la(s)?\\s+)?)?({BaseDateTime.HourRegex}|{TimeHourNumRegex})(\\s*(?<leftDesc>{DescRegex}))?\\s*{TillRegex}\\s*({BaseDateTime.HourRegex}|{TimeHourNumRegex})\\s*(?<rightDesc>{PmRegex}|{AmRegex}|{DescRegex})?'
    PureNumBetweenAnd = f'(entre\\s+(la(s)?\\s+)?)({BaseDateTime.HourRegex}|{TimeHourNumRegex})(\\s*(?<leftDesc>{DescRegex}))?\\s*y\\s*(la(s)?\\s+)?({BaseDateTime.HourRegex}|{TimeHourNumRegex})\\s*(?<rightDesc>{PmRegex}|{AmRegex}|{DescRegex})?'
    TimeRegexWithDotConnector = f'({BaseDateTime.HourRegex}(\\s*\\.\\s*){BaseDateTime.MinuteRegex})'
    SpecificTimeFromTo = f'({RangePrefixRegex})?(?<time1>(({TimeRegex2}|{TimeRegexWithDotConnector}(\\s*{DescRegex})?)|({BaseDateTime.HourRegex}|{TimeHourNumRegex})(\\s*(?<leftDesc>{DescRegex}))?))\\s*{TillRegex}\\s*(?<time2>(({TimeRegex2}|{TimeRegexWithDotConnector}(\\s*{DescRegex})?)|({BaseDateTime.HourRegex}|{TimeHourNumRegex})(\\s*(?<rightDesc>{DescRegex}))?))'
    SpecificTimeBetweenAnd = f'({BetweenRegex})(?<time1>(({TimeRegex1}|{TimeRegex2}|{TimeRegexWithDotConnector}(\\s*{DescRegex})?)|({BaseDateTime.HourRegex}|{TimeHourNumRegex})(\\s*(?<leftDesc>{DescRegex}))?))\\s*{ConnectorAndRegex}\\s*(?<time2>(({TimeRegex1}|{TimeRegex2}|{TimeRegexWithDotConnector}(\\s*{DescRegex})?)|({BaseDateTime.HourRegex}|{TimeHourNumRegex})(\\s*(?<rightDesc>{DescRegex}))?))'
    TimeUnitRegex = f'([^A-Za-z]{{1,}}|\\b)(?<unit>horas|hora|h|minutos|minuto|mins|min|segundos|segundo|secs|sec)\\b'
    TimeFollowedUnit = f'^\\s*{TimeUnitRegex}'
    TimeNumberCombinedWithUnit = f'\\b(?<num>\\d+(\\,\\d*)?)\\s*{TimeUnitRegex}'
    DateTimePeriodNumberCombinedWithUnit = f'\\b(?<num>\\d+(\\.\\d*)?)\\s*{TimeUnitRegex}'
    PeriodTimeOfDayWithDateRegex = f'\\b(((y|a|en|por)\\s+(la\\s+)?|al\\s+)?(((?<early>primeras\\s+horas\\s+)|(?<late>(últimas|altas)\\s+horas\\s+))?(de\\s+la\\s+)?(?<timeOfDay>(mañana|madrugada|(pasado\\s+(el\\s+)?)?medio\\s?d[ií]a|tarde|noche|anoche))))(\\s+(del|de))?\\b'
    RelativeTimeUnitRegex = f'({PastRegex}|{FutureRegex})\\s+{TimeUnitRegex}'
    LessThanRegex = f'\\b(dentro\\s+de\\s+menos\\s+de)\\b'
    MoreThanRegex = f'\\b(durante\\s+(m[áa]s\\s+)?de)\\b'
    SuffixAndRegex = f'(?<suffix>\\s*(y)\\s+((un|uno|una)\\s+)?(?<suffix_num>media|cuarto))'
    FollowedUnit = f'^\\s*{UnitRegex}'
    DurationNumberCombinedWithUnit = f'\\b(?<num>\\d+(\\,\\d*)?){UnitRegex}'
    AnUnitRegex = f'\\b(un(a)?)\\s+{UnitRegex}'
    DuringRegex = f'^[.]'
    AllRegex = f'\\b(?<all>tod[oa]?\\s+(el|la)\\s+(?<unit>año|mes|semana|d[ií]a))\\b'
    HalfRegex = f'\\b(?<half>medi[oa]\\s+(?<unit>ano|mes|semana|d[íi]a|hora))\\b'
    ConjunctionRegex = f'^[.]'
    InexactNumberRegex = f'\\b(pocos|poco|algo|varios)\\b'
    InexactNumberUnitRegex = f'\\b(pocos|poco|algo|varios)\\s+{UnitRegex}'
    HolidayRegex1 = f'\\b(?<holiday>viernes santo|mi[eé]rcoles de ceniza|martes de carnaval|d[ií]a (de|de los) presidentes?|clebraci[oó]n de mao|año nuevo chino|año nuevo|noche vieja|(festividad de )?los mayos|d[ií]a de los inocentes|navidad|noche buena|d[ií]a de acci[oó]n de gracias|acci[oó]n de gracias|yuandan|halloween|noches de brujas|pascuas)(\\s+(del?\\s+)?({YearRegex}|(?<order>(pr[oó]xim[oa]?|est[ea]|[uú]ltim[oa]?|en))\\s+año))?\\b'
    HolidayRegex2 = f'\\b(?<holiday>(d[ií]a( del?( la)?)? )?(martin luther king|todos los santos|blanco|san patricio|san valent[ií]n|san jorge|cinco de mayo|independencia|raza|trabajador))(\\s+(del?\\s+)?({YearRegex}|(?<order>(pr[oó]xim[oa]?|est[ea]|[uú]ltim[oa]?|en))\\s+año))?\\b'
    HolidayRegex3 = f'\\b(?<holiday>(d[ií]a( del?( las?)?)? )(trabajador|madres?|padres?|[aá]rbol|mujer(es)?|solteros?|niños?|marmota|san valent[ií]n|maestro))(\\s+(del?\\s+)?({YearRegex}|(?<order>(pr[oó]xim[oa]?|est[ea]|[uú]ltim[oa]?|en))\\s+año))?\\b'
    BeforeRegex = f'(antes(\\s+del?(\\s+las?)?)?)'
    AfterRegex = f'(despues(\\s*del?(\\s+las?)?)?)'
    SinceRegex = f'(desde(\\s+(las?|el))?)'
    AroundRegex = f'^[.]'
    PeriodicRegex = f'\\b(?<periodic>a\\s*diario|diariamente|mensualmente|semanalmente|quincenalmente|anualmente)\\b'
    EachExpression = f'cada|tod[oa]s\\s*(l[oa]s)?'
    EachUnitRegex = f'(?<each>({EachExpression})\\s*{UnitRegex})'
    EachPrefixRegex = f'(?<each>({EachExpression})\\s*$)'
    EachDayRegex = f'\\s*({EachExpression})\\s*d[ií]as\\s*\\b'
    BeforeEachDayRegex = f'({EachExpression})\\s*d[ií]as(\\s+a\\s+las?)?\\s*\\b'
    SetEachRegex = f'(?<each>({EachExpression})\\s*)'
    LaterEarlyPeriodRegex = f'\\b(({PrefixPeriodRegex})\\s+(?<suffix>{OneWordPeriodRegex})|({UnspecificEndOfRangeRegex}))\\b'
    RelativeWeekRegex = f'(((la|el)\\s+)?(((esta|este|pr[oó]xim[oa]|[uú]ltim(o|as|os))\\s+semana(s)?)|(semana(s)?\\s+(que\\s+viene|pasad[oa]))))'
    WeekWithWeekDayRangeRegex = f'\\b((({RelativeWeekRegex})((\\s+entre\\s+{WeekDayRegex}\\s+y\\s+{WeekDayRegex})|(\\s+de\\s+{WeekDayRegex}\\s+a\\s+{WeekDayRegex})))|((entre\\s+{WeekDayRegex}\\s+y\\s+{WeekDayRegex})|(de\\s+{WeekDayRegex}\\s+a\\s+{WeekDayRegex})){OfPrepositionRegex}\\s+{RelativeWeekRegex})\\b'
    GeneralEndingRegex = f'^[.]'
    MiddlePauseRegex = f'^[.]'
    PrefixArticleRegex = f'^[\\.]'
    OrRegex = f'^[.]'
    YearPlusNumberRegex = f'\\b(años?\\s+((?<year>(\\d{{2,4}}))|{FullTextYearRegex}))\\b'
    NumberAsTimeRegex = f'^[.]'
    TimeBeforeAfterRegex = f'^[.]'
    DateNumberConnectorRegex = f'^[.]'
    CenturyRegex = f'^[.]'
    DecadeRegex = f'(?<decade>diez|veinte|treinta|cuarenta|cincuenta|sesenta|setenta|ochenta|noventa)'
    DecadeWithCenturyRegex = f'(los\\s+)?((((d[ée]cada(\\s+de)?)\\s+)(((?<century>\\d|1\\d|2\\d)?(?<decade>\\d0))))|a[ñn]os\\s+((((dos\\s+)?mil\\s+)?({WrittenOneHundredToNineHundredRegex}\\s+)?{DecadeRegex})|((dos\\s+)?mil\\s+)?({WrittenOneHundredToNineHundredRegex})(\\s+{DecadeRegex}?)|((dos\\s+)?mil)(\\s+{WrittenOneHundredToNineHundredRegex}\\s+)?{DecadeRegex}?))'
    RelativeDecadeRegex = f'\\b(((el|las?)\\s+)?{RelativeRegex}\\s+(((?<number>[\\d]+)|{WrittenOneToNineRegex})\\s+)?d[eé]cadas?)\\b'
    ComplexDatePeriodRegex = f'^[.]'
    YearSuffix = f'(,?\\s*({YearRegex}|{FullTextYearRegex}))'
    AgoRegex = f'\\b(antes\\s+de\\s+(?<day>hoy|ayer|mañana)|antes)\\b'
    LaterRegex = f'\\b(despu[eé]s|desde\\s+ahora|a\\s+partir\\s+de\\s+(?<day>hoy|ayer|mañana))\\b'
    Tomorrow = 'mañana'
    UnitMap = dict([("años", "Y"),
                    ("año", "Y"),
                    ("meses", "MON"),
                    ("mes", "MON"),
                    ("semanas", "W"),
                    ("semana", "W"),
                    ("dias", "D"),
                    ("dia", "D"),
                    ("días", "D"),
                    ("día", "D"),
                    ("jornada", "D"),
                    ("horas", "H"),
                    ("hora", "H"),
                    ("hrs", "H"),
                    ("hr", "H"),
                    ("h", "H"),
                    ("minutos", "M"),
                    ("minuto", "M"),
                    ("mins", "M"),
                    ("min", "M"),
                    ("segundos", "S"),
                    ("segundo", "S"),
                    ("segs", "S"),
                    ("seg", "S")])
    UnitValueMap = dict([("años", 31536000),
                         ("año", 31536000),
                         ("meses", 2592000),
                         ("mes", 2592000),
                         ("semanas", 604800),
                         ("semana", 604800),
                         ("dias", 86400),
                         ("dia", 86400),
                         ("días", 86400),
                         ("día", 86400),
                         ("horas", 3600),
                         ("hora", 3600),
                         ("hrs", 3600),
                         ("hr", 3600),
                         ("h", 3600),
                         ("minutos", 60),
                         ("minuto", 60),
                         ("mins", 60),
                         ("min", 60),
                         ("segundos", 1),
                         ("segundo", 1),
                         ("segs", 1),
                         ("seg", 1)])
    SpecialYearPrefixesMap = dict([("", "")])
    SeasonMap = dict([("primavera", "SP"),
                      ("verano", "SU"),
                      ("otoño", "FA"),
                      ("invierno", "WI")])
    SeasonValueMap = dict([("SP", 3),
                           ("SU", 6),
                           ("FA", 9),
                           ("WI", 12)])
    CardinalMap = dict([("primer", 1),
                        ("primero", 1),
                        ("primera", 1),
                        ("1er", 1),
                        ("1ro", 1),
                        ("1ra", 1),
                        ("segundo", 2),
                        ("segunda", 2),
                        ("2do", 2),
                        ("2da", 2),
                        ("tercer", 3),
                        ("tercero", 3),
                        ("tercera", 3),
                        ("3er", 3),
                        ("3ro", 3),
                        ("3ra", 3),
                        ("cuarto", 4),
                        ("cuarta", 4),
                        ("4to", 4),
                        ("4ta", 4),
                        ("quinto", 5),
                        ("quinta", 5),
                        ("5to", 5),
                        ("5ta", 5)])
    DayOfWeek = dict([("lunes", 1),
                      ("martes", 2),
                      ("miercoles", 3),
                      ("miércoles", 3),
                      ("jueves", 4),
                      ("viernes", 5),
                      ("sabado", 6),
                      ("domingo", 0),
                      ("lu", 1),
                      ("ma", 2),
                      ("mi", 3),
                      ("ju", 4),
                      ("vi", 5),
                      ("sa", 6),
                      ("do", 0)])
    MonthOfYear = dict([("enero", 1),
                        ("febrero", 2),
                        ("marzo", 3),
                        ("abril", 4),
                        ("mayo", 5),
                        ("junio", 6),
                        ("julio", 7),
                        ("agosto", 8),
                        ("septiembre", 9),
                        ("setiembre", 9),
                        ("octubre", 10),
                        ("noviembre", 11),
                        ("diciembre", 12),
                        ("ene", 1),
                        ("feb", 2),
                        ("mar", 3),
                        ("abr", 4),
                        ("may", 5),
                        ("jun", 6),
                        ("jul", 7),
                        ("ago", 8),
                        ("sept", 9),
                        ("set", 9),
                        ("oct", 10),
                        ("nov", 11),
                        ("dic", 12),
                        ("1", 1),
                        ("2", 2),
                        ("3", 3),
                        ("4", 4),
                        ("5", 5),
                        ("6", 6),
                        ("7", 7),
                        ("8", 8),
                        ("9", 9),
                        ("10", 10),
                        ("11", 11),
                        ("12", 12),
                        ("01", 1),
                        ("02", 2),
                        ("03", 3),
                        ("04", 4),
                        ("05", 5),
                        ("06", 6),
                        ("07", 7),
                        ("08", 8),
                        ("09", 9)])
    Numbers = dict([("cero", 0),
                    ("un", 1),
                    ("una", 1),
                    ("uno", 1),
                    ("dos", 2),
                    ("tres", 3),
                    ("cuatro", 4),
                    ("cinco", 5),
                    ("seis", 6),
                    ("siete", 7),
                    ("ocho", 8),
                    ("nueve", 9),
                    ("diez", 10),
                    ("once", 11),
                    ("doce", 12),
                    ("docena", 12),
                    ("docenas", 12),
                    ("trece", 13),
                    ("catorce", 14),
                    ("quince", 15),
                    ("dieciseis", 16),
                    ("dieciséis", 16),
                    ("diecisiete", 17),
                    ("dieciocho", 18),
                    ("diecinueve", 19),
                    ("veinte", 20),
                    ("ventiuna", 21),
                    ("ventiuno", 21),
                    ("veintiun", 21),
                    ("veintiún", 21),
                    ("veintiuno", 21),
                    ("veintiuna", 21),
                    ("veintidos", 22),
                    ("veintidós", 22),
                    ("veintitres", 23),
                    ("veintitrés", 23),
                    ("veinticuatro", 24),
                    ("veinticinco", 25),
                    ("veintiseis", 26),
                    ("veintiséis", 26),
                    ("veintisiete", 27),
                    ("veintiocho", 28),
                    ("veintinueve", 29),
                    ("treinta", 30)])
    HolidayNames = dict([("padres", ["diadelpadre"]),
                         ("madres", ["diadelamadre"]),
                         ("acciondegracias", ["diadegracias", "diadeacciondegracias", "acciondegracias"]),
                         ("trabajador", ["diadeltrabajador"]),
                         ("delaraza", ["diadelaraza", "diadeladiversidadcultural"]),
                         ("memoria", ["diadelamemoria"]),
                         ("pascuas", ["diadepascuas", "pascuas"]),
                         ("navidad", ["navidad", "diadenavidad"]),
                         ("nochebuena", ["diadenochebuena", "nochebuena"]),
                         ("añonuevo", ["a\u00f1onuevo", "diadea\u00f1onuevo"]),
                         ("nochevieja", ["nochevieja", "diadenochevieja"]),
                         ("yuandan", ["yuandan"]),
                         ("maestro", ["diadelmaestro"]),
                         ("todoslossantos", ["todoslossantos"]),
                         ("niño", ["diadelni\u00f1o"]),
                         ("mujer", ["diadelamujer"])])
    VariableHolidaysTimexDictionary = dict([("padres", "-06-WXX-7-3"),
                                            ("madres", "-05-WXX-7-2"),
                                            ("acciondegracias", "-11-WXX-4-4"),
                                            ("trabajador", "-05-WXX-1-1"),
                                            ("delaraza", "-10-WXX-1-2"),
                                            ("memoria", "-03-WXX-2-4")])
    DoubleNumbers = dict([("mitad", 0.5),
                          ("cuarto", 0.25)])
    DateTokenPrefix = 'en '
    TimeTokenPrefix = 'a las '
    TokenBeforeDate = 'el '
    TokenBeforeTime = 'la '
    UpcomingPrefixRegex = f'.^'
    NextPrefixRegex = f'(pr[oó]xim[oa]|siguiente|{UpcomingPrefixRegex})\\b'
    PastPrefixRegex = f'.^'
    PreviousPrefixRegex = f'([uú]ltim[oa]|{PastPrefixRegex})\\b'
    ThisPrefixRegex = f'(est[ea])\\b'
    RelativeDayRegex = f'(?<relday>((este|pr[oó]ximo|([uú]ltim(o|as|os)))\\s+días)|(días\\s+((que\\s+viene)|pasado)))\\b'
    RestOfDateRegex = f'\\bresto\\s+((del|de)\\s+)?((la|el|est[ae])\\s+)?(?<duration>semana|mes|año|decada)(\\s+actual)?\\b'
    RelativeDurationUnitRegex = f'^[\\.]'
    ReferencePrefixRegex = f'(mism[ao]|aquel)\\b'
    ReferenceDatePeriodRegex = f'\\b{ReferencePrefixRegex}\\s+({DateUnitRegex}|fin\\s+de\\s+semana)\\b'
    FromToRegex = f'\\b(from).+(to)\\b.+'
    SingleAmbiguousMonthRegex = f'^(the\\s+)?(may|march)$'
    UnspecificDatePeriodRegex = f'^[.]'
    PrepositionSuffixRegex = f'\\b(on|in|at|around|for|during|since|from|to)$'
    RestOfDateTimeRegex = f'\\bresto\\s+((del|de)\\s+)?((la|el|est[ae])\\s+)?(?<unit>(día|jornada))(\\s+de\\s+hoy)?\\b'
    SetWeekDayRegex = f'^[\\.]'
    NightRegex = f'\\b(medionoche|noche)\\b'
    CommonDatePrefixRegex = f'^[\\.]'
    DurationUnitRegex = f'^[\\.]'
    DurationConnectorRegex = f'^[.]'
    SuffixAfterRegex = f'^[.]'
    YearPeriodRegex = f'^[.]'
    FutureSuffixRegex = f'\\b(despu[ée]s)\\b'
    WrittenDecades = dict([("", 0)])
    SpecialDecadeCases = dict([("", 0)])
    DefaultLanguageFallback = 'DMY'
    DurationDateRestrictions = [r'hoy']
    EarlyMorningTermList = [r'madrugada']
    MorningTermList = [r'mañana']
    AfternoonTermList = [r'pasado mediodia', r'pasado el mediodia']
    EveningTermList = [r'tarde']
    NightTermList = [r'noche']
    SameDayTerms = [r'hoy', r'el dia']
    PlusOneDayTerms = [r'mañana', r'dia siguiente', r'el dia de mañana', r'proximo dia']
    MinusOneDayTerms = [r'ayer', r'ultimo dia']
    PlusTwoDayTerms = [r'pasado mañana', r'dia despues de mañana']
    MinusTwoDayTerms = [r'anteayer', r'dia antes de ayer']
    MonthTerms = [r'mes', r'meses']
    MonthToDateTerms = [r'mes a la fecha', r'meses a la fecha']
    WeekendTerms = [r'fin de semana']
    WeekTerms = [r'semana']
    YearTerms = [r'año', r'años']
    YearToDateTerms = [r'año a la fecha', r'años a la fecha']
    SpecialCharactersEquivalent = dict([("á", "a"),
                                        ("é", "e"),
                                        ("í", "i"),
                                        ("ó", "o"),
                                        ("ú", "u")])
# pylint: enable=line-too-long
