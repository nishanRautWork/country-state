  //   for (const country of COUNTRIES) {
    //     console.log('This is country: ', country);

    //     // Check for duplicates by slug, iso2, or iso3 individually
    //     const existingSlug = await queryRunner.manager.findOne(CountryEntity, {
    //       where: { slug: country.slug },
    //     });
    //     if (existingSlug) {
    //       console.log(`Duplicate slug found: ${country.slug}`);
    //       continue;
    //     }

    //     const existingIso2 = await queryRunner.manager.findOne(CountryEntity, {
    //       where: { iso2: country.iso2 },
    //     });
    //     if (existingIso2) {
    //       console.log(`Duplicate iso2 found: ${country.iso2}`);
    //       continue;
    //     }

    //     const existingIso3 = await queryRunner.manager.findOne(CountryEntity, {
    //       where: { iso3: country.iso3 },
    //     });
    //     if (existingIso3) {
    //       console.log(`Duplicate iso3 found: ${country.iso3}`);
    //       continue;
    //     }

        // If no duplicates, insert the country