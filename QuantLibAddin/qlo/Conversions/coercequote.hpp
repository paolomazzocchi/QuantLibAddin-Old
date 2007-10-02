
/*
 Copyright (C) 2006, 2007 Eric Ehlers

 This file is part of QuantLib, a free-software/open-source library
 for financial quantitative analysts and developers - http://quantlib.org/

 QuantLib is free software: you can redistribute it and/or modify it
 under the terms of the QuantLib license.  You should have received a
 copy of the license along with this program; if not, please email
 <quantlib-dev@lists.sf.net>. The license is also available online at
 <http://quantlib.org/license.shtml>.

 This program is distributed in the hope that it will be useful, but WITHOUT
 ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 FOR A PARTICULAR PURPOSE.  See the license for more details.
*/

#ifndef qlo_conversions_coercequote_hpp
#define qlo_conversions_coercequote_hpp

#include <qlo/Conversions/coercelibrarydifferent.hpp>
#include <qlo/quotes.hpp>

namespace QuantLibAddin {

    // CoerceQuote: A wrapper for CoerceLibraryDifferent which hard-codes
    // those template parameters that are specific to Handle<Quote>

    template <class ObjectQuote, class LibraryQuote>
    class CoerceQuote : public ObjectHandler::Coerce<
        boost::shared_ptr<ObjectHandler::Object>,
        boost::shared_ptr<LibraryQuote> > {

        Conversion *getConversions() {
            static Conversion conversions[] = {
                objectToLibrary<ObjectQuote, LibraryQuote>,
                handleToLibraryDifferent<QuantLibAddin::Quote, QuantLib::Quote, LibraryQuote>,
                0
            };
            return conversions;
        };
    };

}

#endif

