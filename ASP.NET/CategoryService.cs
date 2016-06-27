using System.Collections.Generic;

namespace FourLevelDemo.Services
{
    public class CategoryService
    {
        public static List<Category> GetCategories()
        {
            return new List<Category>(new[]
            {
                new Category
                {
                    Id = 1,
                    Name = "A1",
                    SubCategories = new List<Category>(new[]
                    {
                        new Category
                        {
                            Id = 101,
                            Name = "A101",
                            SubCategories = new List<Category>(new[]
                            {
                                new Category
                                {
                                    Id = 10101,
                                    Name = "A10101",
                                    SubCategories = new List<Category>(new[]
                                    {
                                        new Category
                                        {
                                            Id = 1010101,
                                            Name = "A1010101",
                                        },
                                        new Category
                                        {
                                            Id = 1010102,
                                            Name = "A1010102",
                                        },
                                        new Category
                                        {
                                            Id = 1010103,
                                            Name = "A1010103",
                                        }
                                    })
                                },
                                new Category
                                {
                                    Id = 10102,
                                    Name = "A10102",
                                    SubCategories = new List<Category>(new[]
                                    {
                                        new Category
                                        {
                                            Id = 1010201,
                                            Name = "A1010201",
                                        },
                                        new Category
                                        {
                                            Id = 1010202,
                                            Name = "A1010202",
                                        },
                                        new Category
                                        {
                                            Id = 1010203,
                                            Name = "A1010203",
                                        }
                                    })
                                },
                                new Category
                                {
                                    Id = 10103,
                                    Name = "A10103",
                                    SubCategories = new List<Category>(new[]
                                    {
                                        new Category
                                        {
                                            Id = 1010301,
                                            Name = "A1010301",
                                        },
                                        new Category
                                        {
                                            Id = 1010302,
                                            Name = "A1010302",
                                        },
                                        new Category
                                        {
                                            Id = 1010303,
                                            Name = "A1010303",
                                        }
                                    })
                                }
                            })
                        },
                           new Category
                        {
                            Id = 102,
                            Name = "A102",
                            SubCategories = new List<Category>(new[]
                            {
                                new Category
                                {
                                    Id = 10201,
                                    Name = "A10201",
                                    SubCategories = new List<Category>(new[]
                                    {
                                        new Category
                                        {
                                            Id = 1020101,
                                            Name = "A1020101",
                                        },
                                        new Category
                                        {
                                            Id = 1020102,
                                            Name = "A1020102",
                                        },
                                        new Category
                                        {
                                            Id = 1020103,
                                            Name = "A1020103",
                                        }
                                    })
                                },
                                new Category
                                {
                                    Id = 10202,
                                    Name = "A10202",
                                    SubCategories = new List<Category>(new[]
                                    {
                                        new Category
                                        {
                                            Id = 1020201,
                                            Name = "A1020201",
                                        },
                                        new Category
                                        {
                                            Id = 1020202,
                                            Name = "A1020202",
                                        },
                                        new Category
                                        {
                                            Id = 1020203,
                                            Name = "A1020203",
                                        }
                                    })
                                },
                                new Category
                                {
                                    Id = 10203,
                                    Name = "A10203",
                                    SubCategories = new List<Category>(new[]
                                    {
                                        new Category
                                        {
                                            Id = 1020301,
                                            Name = "A1020301",
                                        },
                                        new Category
                                        {
                                            Id = 1020302,
                                            Name = "A1020302",
                                        },
                                        new Category
                                        {
                                            Id = 1020303,
                                            Name = "A1020303",
                                        }
                                    })
                                }
                            })
                        }
                    })
                },
                new Category
                {
                    Id = 2,
                    Name = "A2",
                    SubCategories = new List<Category>(new[]
                    {
                        new Category
                        {
                            Id = 201,
                            Name = "A201",
                            SubCategories = new List<Category>(new[]
                            {
                                new Category
                                {
                                    Id = 20101,
                                    Name = "A20101",
                                    SubCategories = new List<Category>(new[]
                                    {
                                        new Category
                                        {
                                            Id = 2010101,
                                            Name = "A2010101",
                                        },
                                        new Category
                                        {
                                            Id = 2010102,
                                            Name = "A2010102",
                                        },
                                        new Category
                                        {
                                            Id = 2010103,
                                            Name = "A2010103",
                                        }
                                    })
                                },
                                new Category
                                {
                                    Id = 20102,
                                    Name = "A20102",
                                    SubCategories = new List<Category>(new[]
                                    {
                                        new Category
                                        {
                                            Id = 2010201,
                                            Name = "A2010201",
                                        },
                                        new Category
                                        {
                                            Id = 2010202,
                                            Name = "A2010202",
                                        },
                                        new Category
                                        {
                                            Id = 2010203,
                                            Name = "A2010203",
                                        }
                                    })
                                },
                                new Category
                                {
                                    Id = 20103,
                                    Name = "A20103",
                                    SubCategories = new List<Category>(new[]
                                    {
                                        new Category
                                        {
                                            Id = 2010301,
                                            Name = "A2010301",
                                        },
                                        new Category
                                        {
                                            Id = 2010302,
                                            Name = "A2010302",
                                        },
                                        new Category
                                        {
                                            Id = 2010303,
                                            Name = "A2010303",
                                        }
                                    })
                                }
                            })
                        },
                        new Category
                        {
                            Id = 202,
                            Name = "A202",
                            SubCategories = new List<Category>(new[]
                            {
                                new Category
                                {
                                    Id = 20201,
                                    Name = "A20201",
                                    SubCategories = new List<Category>(new[]
                                    {
                                        new Category
                                        {
                                            Id = 2020101,
                                            Name = "A2020101",
                                        },
                                        new Category
                                        {
                                            Id = 2020102,
                                            Name = "A2020102",
                                        },
                                        new Category
                                        {
                                            Id = 2020103,
                                            Name = "A2020103",
                                        }
                                    })
                                },
                                new Category
                                {
                                    Id = 20202,
                                    Name = "A20202",
                                    SubCategories = new List<Category>(new[]
                                    {
                                        new Category
                                        {
                                            Id = 2020201,
                                            Name = "A2020201",
                                        },
                                        new Category
                                        {
                                            Id = 2020202,
                                            Name = "A2020202",
                                        },
                                        new Category
                                        {
                                            Id = 2020203,
                                            Name = "A2020203",
                                        }
                                    })
                                },
                                new Category
                                {
                                    Id = 20203,
                                    Name = "A20203",
                                    SubCategories = new List<Category>(new[]
                                    {
                                        new Category
                                        {
                                            Id = 2020301,
                                            Name = "A2020301",
                                        },
                                        new Category
                                        {
                                            Id = 2020302,
                                            Name = "A2020302",
                                        },
                                        new Category
                                        {
                                            Id = 2020303,
                                            Name = "A2020303",
                                        }
                                    })
                                }
                            })
                        }
                    })
                }
            });
        }
    }

    public class Category
    {
        public int Id { get; set; }

        public string Name { get; set; }

        public List<Category> SubCategories { get; set; }
    }
}
